# Reference architectures for the Rackspace platform

This repo holds blueprints that are designed to provide developers and users with the necessary guidance and best practices to build applications on the Rackspace cloud.

## Supported workflows

- [Multi-tiered web app](./web-app)
- [Large-scale batch processing](./batch-processing)
- [Docker micro-services with OnMetal and CoreOS](./docker-onmetal)
- [Distributed eCommerce platform](./ecommerce)

## How to add a new architecture

Each architecture blueprint should try and solve an expected customer workflow: web app content delivery, scaling an eCommerceshop, handling thousands of scientific compute jobs horizontally, transcoding videos, etc. Once you've decided on an expected workflow, you can begin to identify which Rackspace architecture that can solve the problem.

When implementing a new architecture blueprint, there are four steps:

1. Identify the Rackspace architecture that your workflow will use. Draw up a very simple diagram that can help outline how each component operates and integrate together (I use https://draw.io). These will eventually be stylized by our UI team. Another thing you will need to do is define and describe in text how each component works - a brief paragraph will do. Think about its role in the wider problem, what software will be installed, how it will be configured, etc. Be opinionated about best practices.

2. Once you've identified the Rackspace services, think of an example application that can showcase the architecture. We want to make everything less abstract and more concrete, to prove to users that this architecture will work when deployed. You should just focus on a very simple, ubiquitious, "cookie-cutter" open-source application to get the ball rolling. For example, if you're trying to showcase a Web App architecture, you might choose WordPress, Ghost, or Reddit (all open-source) to showcase how everything works.

3. Write deployment scripts (both in Heat and Ansible) that will provision both the infrastructure _and_ software. We want a developer to be able to deploy the full stack quickly and easily.

4. Benchmark the architecture and showcase the results. Optimize the architecture if necessary.

These are the introductory steps that are necessary for a new blueprint. Once we've covered these steps, had everything reviewed, and are comfortable will releasing it, we can look to add more diverse and complicated software examples in the future. For example, if we've used Wordpress, we might want to make it applicable to Ruby or Python devs.

## Contributing

This project has just begun and we'd love as many contributors as possible. Any todo items will be logged as Github issues, so feel free to grab one. If you want to discuss anything, feel free to open a Github issue, email DeveloperExperience@rackspace.com or join the #architectures Slack channel.

#### Four ways to get involved

1. Think of new architectures. For advice, see the above section.
2. Review the content/documentation of an existing architecture, such as grammar and spelling. Look at how we communicate: can we break down complex topics and make them less abstract. We want our content to be understandable and relevant.
3. Write deployment scripts in Ansible and Heat
4. Test the deployment scripts and help with benchmarking
