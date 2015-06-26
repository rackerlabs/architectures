import pyrax
import yaml
import sys
import os

config_yml = yaml.load(open("vars.yml"))

pyrax.set_setting("identity_type", "rackspace")
pyrax.set_credentials(config_yml['username'], config_yml['api_key'])

region = config_yml["rs_region"] if config_yml["rs_region"] else "IAD"
cs = pyrax.connect_to_cloudservers(region=region)

img_id = None

servers = cs.servers.list()
for server in servers:
  if server.name == 'blueprint':
    img_id = server.create_image("autoscale_blueprint")
    break

if img_id is None:
  print "No server named `blueprint`"
  sys.exit(1)

img = cs.images.get(img_id)
img = pyrax.utils.wait_until(img, "status", ["ACTIVE", "ERROR"], attempts=0)

output_file = os.path.dirname(os.path.realpath(__file__)) + "/.img_id"

f = open(output_file, "w")
f.write(img_id)
f.close()

server.delete()
