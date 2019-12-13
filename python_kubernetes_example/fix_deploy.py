#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 15:59
# @Author  : shenhao
# @File    : fix_deploy.py
from kubernetes import client

DEPLOYMENT_NAME = "nginx-deployment"


def create_deployment_object():
    # Configureate Pod template container
    container = client.V1Container(
        name="nginx",
        image="nginx:1.10",
        ports=[client.V1ContainerPort(container_port=80)])
    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "nginx"}),
        spec=client.V1PodSpec(containers=[container]))
    # Create the specification of deployment
    spec = client.V1DeploymentSpec(
        replicas=3,
        template=template,
        selector={'matchLabels': {'app': 'nginx'}})
    # Instantiate the deployment object
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=DEPLOYMENT_NAME),
        spec=spec)

    return deployment


def create_deployment(api_instance, deployment):
    # Create deployement
    api_response = api_instance.create_namespaced_deployment(
        body=deployment,
        namespace="default")
    print("Deployment created. status='%s'" % str(api_response.status))


def update_deployment(api_instance, deployment):
    # Update container image
    deployment.spec.replicas = 1
    # Update the deployment
    api_response = api_instance.patch_namespaced_deployment(
        name=DEPLOYMENT_NAME,
        namespace="default",
        body=deployment)
    print("Deployment updated. status='%s'" % str(api_response.status))


def delete_deployment(api_instance):
    # Delete deployment
    api_response = api_instance.delete_namespaced_deployment(
        name=DEPLOYMENT_NAME,
        namespace="default",
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=5))
    print("Deployment deleted. status='%s'" % str(api_response.status))


def main():
    with open('token.txt', 'r') as file:
        Token = file.read().strip('\n')

    APISERVER = 'https://21.254.248.80:6443'

    configuration = client.Configuration()

    configuration.host = APISERVER

    configuration.verify_ssl = False

    configuration.api_key = {"authorization": "Bearer " + Token}

    client.Configuration.set_default(configuration)

    apps_v1 = client.AppsV1Api()

    deployment = create_deployment_object()

    # create_deployment(apps_v1, deployment)
    #
    update_deployment(apps_v1, deployment)
    #
    # delete_deployment(apps_v1)


if __name__ == '__main__':
    main()
