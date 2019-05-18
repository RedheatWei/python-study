#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/6 13:20'
@email = 'qjyyn@qq.com'
'''
'''
k8s apiserver认证
'''
from kubernetes import client, config

# see https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/#accessing-the-cluster-api to know how to get the token
# The command look like kubectl get secrets | grep default | cut -f1 -d ' ') | grep -E '^token' | cut -f2 -d':' | tr -d '\t' but better check the official doc link
# aToken="token-trt2j:ch5k2k2g67f4wx5ss4w5m8glbfhq2n5572gvm2v67844wxld7nc54c"
aToken="kubeconfig-user-sm8tm:ms8q46bghd2mkdfm5rf8dr6q664bl7qlfzf2srmcdd8lqlh6cqbvgp"
# Configs can be set in Configuration class directly or using helper utility
configuration = client.Configuration()
configuration.host = "https://rancher.evbj.easou.com/k8s/clusters/local"
configuration.verify_ssl = False
# configuration.debug = True

# Maybe there is a way to use these options instead of token since they are provided in Google cloud UI
configuration.api_key = {"authorization": "Bearer " + aToken}
client.Configuration.set_default(configuration)

v1 = client.CoreV1Api()
ret = v1.list_namespace()
print(ret)
# for i in ret.groups:
#     print(i.name)