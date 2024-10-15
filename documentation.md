# Ports documentation
Port 6000 is used inside the container where the React app is running. This is where the React app listens for requests.

Port 8088 is on the local machine , and thanks to the configuration of the k3d cluster, it is mapped to port 80 of the Kubernetes LoadBalancer service inside the cluster.



# Accessing database
Get the name of the pod:
``kubectl get pods --namespace=systems-pe-namespace``

Open shell into the pod
``kubectl exec -it <postgres-pod-name> --namespace=systems-pe-namespace -- bash``

Access the database
``psql -U myname -d mydatabase``
- ``-U myname`` specifies the username
- ``-d mydatabase`` specifies the database name
- The password is provided as an environment variable when the container starts. This password is automatically passed when running the psql command. No need to manually input the password.

List all tables
``\dt`

Query the contents of the table
``SELECT * FROM text;``

&nbsp;

# Password documentation
Base64 encoding is required to store secrets and Kubernetes automatically decodes them when the pod is running.

Retrieve the password from the pod
``kubectl exec -it flask-backend-<pod-name> --namespace=systems-pe-namespace -- env | grep DATABASE_PASSWORD``

Base64 encoding a password
``echo -n "mypassword" | base64``

Base64 decoding a password
``echo -n "bXlwYXNzd29yZA==" | base64 --decode``

&nbsp;

# Error documentation
- **500 error on frontend**: Frontend returned 500 error due to an incorrect database connection URI.
    - Corrected the database connection string in the backend by properly concatenating the environment variables, ensuring the correct DATABASE_URI was passed from the ConfigMap.
- **Proxy port 4000 error in frontend**: Misconfiguration in the port mapping, causing the frontend to fail when trying to proxy requests to port 4000 on the backend.
    - Adjusted the frontend configuration to correctly point to the backend service on the right port. Also ensured the backend service was exposed with the correct target port.
- **DaemonSet 0/2 issue in Lens (loadbalancer port conflict)**: DaemonSet for the load balancer was showing as 0/2 in Lens, indicating that it couldn't allocate the necessary ports due to a port conflict.
    - Adjusted the LoadBalancer service configuration, specifically by changing the port mapping in the Service YAML file to resolve the conflict. This fixed the DaemonSet scheduling issue.
- **HELM and Traefik errors due to Namespace deletion**: Every time the setup.sh script was run, Helm and Traefik components were being deleted because the entire namespace was being deleted. This caused Helm to fail on subsequent runs.
    - Modified the setup.sh script to selectively delete only the application's deployments, services, ConfigMaps, and Secrets, while preserving the namespace and system-level components like Helm and Traefik. This avoided the need to reinstall Helm and Traefik every time.
- **MountVolume.SetUp failed for volume 'values' (Traefik warning)**: A warning appeared regarding MountVolume.SetUp failed for volume "values" in the Traefik installation due to a failure to sync the secret cache.
    - This error was determined to be related to the Helm/Tiller component and not directly caused by the application setup. As it did not affect the functionality of the app, it was considered safe to ignore for this project.
- **Readiness probe failed (HTTP Probe 500 Error on metrics server)**: A readiness probe failed on the metrics-server pod, showing an HTTP 500 error.
    - This error was related to the metrics server and not directly tied to the app's core functionality. Since the app itself was unaffected, it was noted as a non-blocking issue.
- **Failed to sync secret cache (database connection refused)**: The backend service was showing connection refused errors when trying to connect to the PostgreSQL database. This was caused by an incorrect or outdated secret being used for the database password.
    - The issue was resolved by recreating the Kubernetes Secret containing the database password. The pods were then restarted to ensure they picked up the updated secret values.
- **Incorrect password in secret**: After changing the database password, the app was still using the old password from the secret, leading to authentication issues.
    - Deleted and recreated the Kubernetes Secret with the correct password. The backend and PostgreSQL pods were restarted to ensure they used the updated secret.

&nbsp;