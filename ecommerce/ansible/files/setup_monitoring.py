import pyrax
import getopt
import sys
import os
import yaml

try:
    opts, args = getopt.getopt(sys.argv[1:], "gud", ["group=", "up=", "down="])
except:
    print str(err)
    usage()
    sys.exit(2)

up_policy_id = None
down_policy_id = None

for o, a in opts:
    if o in ('-g', '--group'):
        group_id = a
    elif o in ('-u', '--up'):
        up_policy_id = a
    elif o in ('-d', '--down'):
        down_policy_id = a

config_yml = yaml.load(open("vars.yml"))

pyrax.set_setting("identity_type", "rackspace")
pyrax.set_credentials(config_yml['username'], config_yml['api_key'])

region = config_yml["rs_region"] if config_yml["rs_region"] else "IAD"

cm = pyrax.cloud_monitoring
au = pyrax.connect_to_autoscale(region=region)

policy = au.get(group_id)

# Create webhook for UP policy
up = policy.get_policy(up_policy_id)
up_hook = up.add_webhook("default")

# Create webhook for DOWN policy
down = policy.get_policy(down_policy_id)
down_hook = down.add_webhook("default")

# Extract capability URLs
down_hook_link = None
up_hook_link = None

for l in down_hook.links:
    if l["rel"] == 'capability':
        down_hook_link = l["href"]

for l in up_hook.links:
    if l["rel"] == 'capability':
        up_hook_link = l["href"]

# Create CRITICAL notification
cr_n = cm.create_notification("webhook", label="critical", details={"url": up_hook_link})

# Create OK notification
ok_n = cm.create_notification("webhook", label="OK", details={"url": down_hook_link})

# Create notification plan
plan = cm.create_notification_plan(label="production", ok_state=ok_n, critical_state=cr_n)

output_file = os.path.dirname(os.path.realpath(__file__)) + "/.np_id"

f = open(output_file, 'w')
f.write(plan.id)
f.close()
