import pyrax
import yaml
import sys

config_yml = yaml.load(open("vars.yml"))

pyrax.set_setting("identity_type", "rackspace")
pyrax.set_credentials(config_yml['username'], config_yml['api_key'])

region = config_yml["region"] if config_yml["region"] else "IAD"
cs = pyrax.connect_to_cloudservers(region=region)

img_id = None

servers = cs.servers.list()
for server in servers:
  if server.name == 'blueprint':
    img_id = server.create_image("autoscale_blueprint")

if img_id is None:
  print "No server named `blueprint`"
  sys.Exit(1)

img = cs.images.get(img_id)
img = pyrax.utils.wait_until(img, "status", ["ACTIVE", "ERROR"], attempts=0)

output_file = "roles/blueprint-image/files/.img_id"

f = open(output_file, "w")
f.write(img_id)
f.close()
