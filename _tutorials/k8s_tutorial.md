---
title: "Kubernetes Tutorial"
description: "Notes and thoughts about the official Kubernetes tutorial"
last_update: "2020-05-1125"
published: false
---
# Kubernetes Tutorial
###### Last Updated: {{ page.last_update | date: "%A, %B %d, %Y" }}

This article contains my notes collected while following the [official Kubernetes Tutorials](https://kubernetes.io/docs/tutorials/).

The main reason for it is that the official tutorials use an online Minikube environment, while I ran them using the quasi-production environment setup in a previous tutorial.

> **WARNING** : During my tests I discovered that apparently there is no way to easily shutdown a kubernetes cluster. While this is quite expected and desirable in a production environment (after all one of the main points about Kubernetes is to provide resilience), this creates some problem in our little test environment, where we are supposed to shutdown our laptop every day. I discovered that when I do that, the next day the VMs have problems to start and (when they do) the whole kubernetes cluster is gone south. This is not a problem in the official tutorial, because they restart the whole environment every time, so everything is fresh. After few researches, I decided to approach the problem in the following way:

> I create a namespace for testing with `kubectl create ns k8s_tutorial`. They I will follow the official tutorial in this namespace (by adding `-n k8s_tutorial` to the commands). Once I've finished (or before to shutdown), I just issue a `kubectl delete ns k8s_tutorial` and I'm done.

> A side effect of this is that details about running pods and similar information will not be consistent across this tutorial. I'm sorry for that. I will try to fix the issue in the future.

> In order to facilitate my explorative tests splitting them over multiple days, I created a `start_k8s_tutorial.sh` and `stop_k8s_tutorial.sh` scripts which you can find details at the end of this tutorial.

## 1 - Create a Kubernetes cluster

Let's check that `kubectl` is installed. On the `k8sMaster` execute

```
aizzi@k8sMaster:~$ kubectl version
Client Version: version.Info{Major:"1", Minor:"18", GitVersion:"v1.18.3", GitCommit:"2e7996e3e2712684bc73f0dec0200d64eec7fe40", GitTreeState:"clean", BuildDate:"2020-05-20T12:52:00Z", GoVersion:"go1.13.9", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{Major:"1", Minor:"18", GitVersion:"v1.18.3", GitCommit:"2e7996e3e2712684bc73f0dec0200d64eec7fe40", GitTreeState:"clean", BuildDate:"2020-05-20T12:43:34Z", GoVersion:"go1.13.9", Compiler:"gc", Platform:"linux/amd64"}
```

Note that the same command executed on `k8sNode1` returns only the Client Version, which is fine because we have not configured the control plane on it.

```
aizzi@k8sNode1:~$ kubectl version
Client Version: version.Info{Major:"1", Minor:"18", GitVersion:"v1.18.3", GitCommit:"2e7996e3e2712684bc73f0dec0200d64eec7fe40", GitTreeState:"clean", BuildDate:"2020-05-20T12:52:00Z", GoVersion:"go1.13.9", Compiler:"gc", Platform:"linux/amd64"}
The connection to the server localhost:8080 was refused - did you specify the right host or port?
```

Pay attention to the version on Client and Server, because Kubernets is very strict about the alignment of components throughtout the cluster.

To check cluster's details, on the `k8sMaster` execute:

```
aizzi@k8sMaster:~$ kubectl cluster-info
Kubernetes master is running at https://192.168.56.10:6443
KubeDNS is running at https://192.168.56.10:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```

Let's see all nodes that can be used to host our applications:

```
aizzi@k8sMaster:~$ kubectl get nodes
NAME        STATUS   ROLES    AGE   VERSION
k8smaster   Ready    master   29m   v1.18.3
k8snode1    Ready    <none>   22m   v1.18.3
```

## 2 - Using kubectl to Create a Deployment

To deploy an application into the above cluster, we must create a `Deployment` configuration. A `Deployment` instructs Kubernetes about how to create and update instances of our application. The Kubernetes master schedules the application instances included in the `Deployment` to run on individual Nodes in the cluster.

Once the application is deployed, the Kubernetes Deployment Controller continuously monitors it. If the Node hosting it goes down or is deleted, the Deployment Controller replaces the instance with an instance on another Node in the cluster.

In this tutorial you will use `kubectl` to create a Deployment.

Type `kubectl` on `k8sMaster` to see how to use it. The common format of a kubectl command is `kubectl action resource`. You can use `--help` after the command to get additional info about possible parameters.

You can deploy your first app on Kubernetes with the `kubectl create deployment` command. You need to provide the deployment name and app image location (including the full repository url for images hosted outside Docker hub)

```
aizzi@k8sMaster:~$ kubectl create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1 -n k8s-tutorial 
deployment.apps/kubernetes-bootcamp created
```

The above command:

* searched for a suitable node where an instance of the application could be run
* scheduled the application to run on that node
* configured the cluster to reschedule the instance on a new Node when needed

To list your deployments:

```
aizzi@k8sMaster:~$ kubectl get deployments -n k8s-tutorial
NAME                  READY   UP-TO-DATE   AVAILABLE   AGE
kubernetes-bootcamp   1/1     1            1           48s
```

We can use the same command to describe pods:

```
aizzi@k8sMaster:~$ kubectl get pods -n k8s-tutorial
NAME                                   READY   STATUS    RESTARTS   AGE
kubernetes-bootcamp-6f6656d949-9q9hz   1/1     Running   0          14m
```

We can get all the resources running under a defined namespace with the following command:

```
aizzi@k8sMaster:~$ kubectl get all -n k8s-tutorial
NAME                                       READY   STATUS    RESTARTS   AGE
pod/kubernetes-bootcamp-6f6656d949-tvh4z   1/1     Running   0          74s

NAME                                  READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/kubernetes-bootcamp   1/1     1            1           74s

NAME                                             DESIRED   CURRENT   READY   AGE
replicaset.apps/kubernetes-bootcamp-6f6656d949   1         1         1       74s
```

and we can get details about the running pod:

```
aizzi@k8sMaster:~$ kubectl describe pod/kubernetes-bootcamp-6f6656d949-tvh4z -n k8s-tutorial
Name:         kubernetes-bootcamp-6f6656d949-tvh4z
Namespace:    k8s-tutorial
Priority:     0
Node:         k8snode1/10.0.2.15
Start Time:   Thu, 04 Jun 2020 09:52:36 +0000
Labels:       app=kubernetes-bootcamp
              pod-template-hash=6f6656d949
Annotations:  cni.projectcalico.org/podIP: 192.168.249.5/32
              cni.projectcalico.org/podIPs: 192.168.249.5/32
Status:       Running
IP:           192.168.249.5
IPs:
  IP:           192.168.249.5
Controlled By:  ReplicaSet/kubernetes-bootcamp-6f6656d949
Containers:
  kubernetes-bootcamp:
    Container ID:   docker://c02fe41f8b13914506bfb5c19ba75ceec3dafd3358e38aa132786ac7dc175367
    Image:          gcr.io/google-samples/kubernetes-bootcamp:v1
    Image ID:       docker-pullable://gcr.io/google-samples/kubernetes-bootcamp@sha256:0d6b8ee63bb57c5f5b6156f446b3bc3b3c143d233037f3a2f00e279c8fcc64af
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Thu, 04 Jun 2020 09:52:37 +0000
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-8nnks (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  default-token-8nnks:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-8nnks
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  <none>
Tolerations:     node.kubernetes.io/not-ready:NoExecute for 300s
                 node.kubernetes.io/unreachable:NoExecute for 300s
Events:
  Type    Reason     Age        From               Message
  ----    ------     ----       ----               -------
  Normal  Scheduled  <unknown>  default-scheduler  Successfully assigned k8s-tutorial/kubernetes-bootcamp-6f6656d949-tvh4z to k8snode1
  Normal  Pulled     2m46s      kubelet, k8snode1  Container image "gcr.io/google-samples/kubernetes-bootcamp:v1" already present on machine
  Normal  Created    2m46s      kubelet, k8snode1  Created container kubernetes-bootcamp
  Normal  Started    2m46s      kubelet, k8snode1  Started container kubernetes-bootcamp
```

Pods running inside Kubernetes are running on a private, isolated network. By default they are visible from other pods and services within the same kubernetes cluster, but not outside that network.

From the above, we can see that the pod is running on the 'k8snode1' with the address '192.168.249.5'. We can ping this address from 'k8sMaster' and 'k8sNode1', but if we try to access it from our host machine (outside of the kubernetes cluster), we cannot access it:

'''
C:\Users\aizzi>ping 192.168.249.3

Pinging 192.168.249.3 with 32 bytes of data:
Request timed out.
Request timed out.
Request timed out.
Request timed out.

Ping statistics for 192.168.249.3:
    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),
'''

In order to expose the pod to the world, the 'kubectl' command can create a proxy that will forward communications into the cluster-wide, private network. Let's start it with the following command:

'''
aizzi@k8sMaster:~$ kubectl proxy --address='192.168.56.10' --accept-hosts='^.*'
Starting to serve on 192.168.56.10:8001
'''

The `--address` option is needed to serve on the right address; the `--accept-hosts` is needed to accept the connection (*I tried several combinations without much success, and this one worked so I will investigate deeper at a later time*).

Now we can connect to the `kubectl` proxy from the host machine:

```
C:\Users\aizzi>curl http://k8smaster:8001/version
{
  "major": "1",
  "minor": "18",
  "gitVersion": "v1.18.3",
  "gitCommit": "2e7996e3e2712684bc73f0dec0200d64eec7fe40",
  "gitTreeState": "clean",
  "buildDate": "2020-05-20T12:43:34Z",
  "goVersion": "go1.13.9",
  "compiler": "gc",
  "platform": "linux/amd64"
}
```

## 3 - Exploring Your App

A kubernetes pod can be considered as a "virtual server" running on the kubernets node. Each pod contains one or more containers, storage, volumes as well as networking.

> **Note** : it seems there is a problem with running the tutorial outside of the official environment. You can find details [here](https://github.com/kubernetes/website/issues/18079)

First of all, let's get the name of the POD:

```
aizzi@k8sMaster:~$ kubectl get pod -n k8s-tutorial -o wide
NAME                                   READY   STATUS    RESTARTS   AGE   IP              NODE       NOMINATED NODE   READINESS GATES
kubernetes-bootcamp-6f6656d949-nhj9w   1/1     Running   0          57s   192.168.249.1   k8snode1   <none>           <none>
aizzi@k8sMaster:~$ export POD_NAME=kubernetes-bootcamp-6f6656d949-nhj9w
aizzi@k8sMaster:~$ echo $POD_NAME
kubernetes-bootcamp-6f6656d949-nhj9w
```

Now, open a new terminal and start the proxy on `localhost`:

```
aizzi@k8sMaster:~$ kubectl proxy
Starting to serve on 127.0.0.1:8001
```

Open a command line on the host machine and issue the following command:

```
aizzi@k8sMaster:~$ curl http://localhost:8001/api/v1/namespaces/k8s-tutorial/pods/$POD_NAME:8080/proxy/
Hello Kubernetes bootcamp! | Running on: kubernetes-bootcamp-6f6656d949-nhj9w | v=1
```

We can retrieve the logs using the `kubectl logs` command:

```
aizzi@k8sMaster:~$ kubectl logs $POD_NAME -n k8s-tutorial
Kubernetes Bootcamp App Started At: 2020-06-04T14:26:13.207Z | Running On:  kubernetes-bootcamp-6f6656d949-nhj9w

Running On: kubernetes-bootcamp-6f6656d949-nhj9w | Total Requests: 1 | App Uptime: 226.639 seconds | Log Time: 2020-06-04T14:29:59.846Z
```

We can execute commands directly on the container once the Pod is up and running, using the `exec` command:

```
aizzi@k8sMaster:~$ kubectl exec $POD_NAME -n k8s-tutorial -- env
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=kubernetes-bootcamp-6f6656d949-nhj9w
KUBERNETES_SERVICE_PORT_HTTPS=443
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_PORT=443
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_SERVICE_PORT=443
NPM_CONFIG_LOGLEVEL=info
NODE_VERSION=6.3.1
HOME=/root
```

We can start a bash session inside the Pod's container:

```
aizzi@k8sMaster:~$ kubectl exec -ti $POD_NAME -n k8s-tutorial -- bash
root@kubernetes-bootcamp-6f6656d949-nhj9w:/# ls
bin  boot  core  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  server.js  srv  sys  tmp  usr  var

root@kubernetes-bootcamp-6f6656d949-nhj9w:/# cat server.js
var http = require('http');
var requests=0;
var podname= process.env.HOSTNAME;
var startTime;
var host;
var handleRequest = function(request, response) {
  response.setHeader('Content-Type', 'text/plain');
  response.writeHead(200);
  response.write("Hello Kubernetes bootcamp! | Running on: ");
  response.write(host);
  response.end(" | v=1\n");
  console.log("Running On:" ,host, "| Total Requests:", ++requests,"| App Uptime:", (new Date() - startTime)/1000 , "seconds", "| Log Time:",new Date());
}
var www = http.createServer(handleRequest);
www.listen(8080,function () {
    startTime = new Date();;
    host = process.env.HOSTNAME;
    console.log ("Kubernetes Bootcamp App Started At:",startTime, "| Running On: " ,host, "\n" );
});

root@kubernetes-bootcamp-6f6656d949-nhj9w:/# curl localhost:8080
Hello Kubernetes bootcamp! | Running on: kubernetes-bootcamp-6f6656d949-nhj9w | v=1

root@kubernetes-bootcamp-6f6656d949-nhj9w:/# exit
exit
```

## 4 - Expose your app publicly

To create a new service and expose it to external traffic we'll use the expose command with NodePort as parameter:

```
aizzi@k8sMaster:~$ kubectl get deployments -n k8s-tutorial -o wide
NAME                  READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS            IMAGES                                         SELECTOR
kubernetes-bootcamp   1/1     1            1           41m   kubernetes-bootcamp   gcr.io/google-samples/kubernetes-bootcamp:v1   app=kubernetes-bootcamp

aizzi@k8sMaster:~$ kubectl get pods -n k8s-tutorial -o wide
NAME                                   READY   STATUS    RESTARTS   AGE   IP              NODE       NOMINATED NODE   READINESS GATES
kubernetes-bootcamp-6f6656d949-gvlbn   1/1     Running   0          42m   192.168.249.3   k8snode1   <none>           <none>

aizzi@k8sMaster:~$ kubectl expose deployment/kubernetes-bootcamp -n k8s-tutorial --type="NodePort" --port 8080
service/kubernetes-bootcamp exposed

aizzi@k8sMaster:~$ kubectl get service -n k8s-tutorial -o wide
NAME                  TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE     SELECTOR
kubernetes-bootcamp   NodePort   10.109.158.67   <none>        8080:31592/TCP   2m25s   app=kubernetes-bootcamp

aizzi@k8sMaster:~$ kubectl describe service -n k8s-tutorial kubernetes-bootcamp
Name:                     kubernetes-bootcamp
Namespace:                k8s-tutorial
Labels:                   app=kubernetes-bootcamp
Annotations:              <none>
Selector:                 app=kubernetes-bootcamp
Type:                     NodePort
IP:                       10.109.158.67
Port:                     <unset>  8080/TCP
TargetPort:               8080/TCP
NodePort:                 <unset>  31592/TCP
Endpoints:                192.168.249.3:8080
Session Affinity:         None
External Traffic Policy:  Cluster
Events:                   <none>
```

So, let's see our option to reach the container. We can get to it from inside the cluster by accessing port 8080 on the Pod's address:

```
aizzi@k8sMaster:~$ curl 192.168.249.3:8080
Hello Kubernetes bootcamp! | Running on: kubernetes-bootcamp-6f6656d949-gvlbn | v=1
```

or we can reach it from inside the cluster through the service

```
aizzi@k8sMaster:~$ curl 10.109.158.67:8080
Hello Kubernetes bootcamp! | Running on: kubernetes-bootcamp-6f6656d949-gvlbn | v=1
```

If we are outside the cluster, though, we can only reach the nodes. In that case, we can reach it through the exposed port:

```
C:\Users\CZ100003>curl 192.168.56.10:31592
Hello Kubernetes bootcamp! | Running on: kubernetes-bootcamp-6f6656d949-gvlbn | v=1

C:\Users\CZ100003>curl 192.168.56.11:31592
Hello Kubernetes bootcamp! | Running on: kubernetes-bootcamp-6f6656d949-gvlbn | v=1
```

Please, note that the above commands were issued from the host machine, completely outside of the kubernetes cluster.

The deployment created automatically a label. We can use it to query our list of Pods as well as any other element:

```
aizzi@k8sMaster:~$ kubectl get pods -l app=kubernetes-bootcamp -n k8s-tutorial -o wide
NAME                                   READY   STATUS    RESTARTS   AGE   IP              NODE       NOMINATED NODE   READINESS GATES
kubernetes-bootcamp-6f6656d949-gvlbn   1/1     Running   0          54m   192.168.249.3   k8snode1   <none>           <none>

aizzi@k8sMaster:~$ kubectl get services -l app=kubernetes-bootcamp -n k8s-tutorial -o wide
NAME                  TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE   SELECTOR
kubernetes-bootcamp   NodePort   10.109.158.67   <none>        8080:31592/TCP   30m   app=kubernetes-bootcamp
```

To apply a new label we use the label command followed by the object type, object name and the new label:

```
aizzi@k8sMaster:~$ kubectl label pod kubernetes-bootcamp-6f6656d949-gvlbn -n k8s-tutorial version=v1
pod/kubernetes-bootcamp-6f6656d949-gvlbn labeled

aizzi@k8sMaster:~$ kubectl describe pod -n k8s-tutorial kubernetes-bootcamp-6f6656d949-gvlbn
Name:         kubernetes-bootcamp-6f6656d949-gvlbn
Namespace:    k8s-tutorial
Priority:     0
Node:         k8snode1/192.168.56.11
Start Time:   Thu, 04 Jun 2020 15:18:38 +0000
Labels:       app=kubernetes-bootcamp
              pod-template-hash=6f6656d949
              version=v1
...
```

and we can use the new label to access the pod:

```
aizzi@k8sMaster:~$ kubectl get pods -l version=v1 -n k8s-tutorial -o wide
NAME                                   READY   STATUS    RESTARTS   AGE   IP              NODE       NOMINATED NODE   READINESS GATES
kubernetes-bootcamp-6f6656d949-gvlbn   1/1     Running   0          59m   192.168.249.3   k8snode1   <none>           <none>
```

To delete the service we can use the `delete service` command:

```
aizzi@k8sMaster:~$ kubectl get services -l app=kubernetes-bootcamp -n k8s-tutorial -o wide
NAME                  TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE   SELECTOR
kubernetes-bootcamp   NodePort   10.109.158.67   <none>        8080:31592/TCP   35m   app=kubernetes-bootcamp

aizzi@k8sMaster:~$ kubectl delete services -l app=kubernetes-bootcamp -n k8s-tutorial
service "kubernetes-bootcamp" deleted

aizzi@k8sMaster:~$ kubectl get services -l app=kubernetes-bootcamp -n k8s-tutorial -o wide
No resources found in k8s-tutorial namespace.
```

Now, I cannot connect anymore to the application from outside the cluster:

```
C:\Users\CZ100003>curl 192.168.56.11:31592
curl: (7) Failed to connect to 192.168.56.11 port 31592: Connection refused

C:\Users\CZ100003>curl 192.168.56.10:31592
curl: (7) Failed to connect to 192.168.56.10 port 31592: Connection refused
```

but I can still access it from inside:

```
aizzi@k8sMaster:~$ curl 192.168.249.3:8080
Hello Kubernetes bootcamp! | Running on: kubernetes-bootcamp-6f6656d949-gvlbn | v=1
```
