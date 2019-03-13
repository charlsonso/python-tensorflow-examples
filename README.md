tb_script.py

example script to run tensorboard. use the command

```tensorboard --logdir tb_logs/ --host localhost --port 6006 ```

to visualize the graph.

Use 
```ssh -N -L localhost:8887:0.0.0.0:6006 username@remote_server```
for port forwarding. 
