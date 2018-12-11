# -*- coding: utf-8 -*-
"""
Created on 2018-4-17

@author: ros
"""
import flask

app = flask.Flask(__name__)



@app.route('/cloud_service/<service>/<action>', methods=['POST'])
def cloud_service(service,action):
    ros_master_ip = flask.request.remote_addr
    ros_master_uri = 'http://'+ros_master_ip+':11311'
    os.environ['ROS_MASTER_URI']=ros_master_uri
    os.environ['ROS_IP']=cloud_ip
    if action == 'start':
        thread.start_new_thread(service_start,(service,))
        time.sleep(5)
        return "service " + service + " starting"
    elif action == 'stop':
       os.system('sh ~/catkin_ws/src/cloud_v2/scripts/stop.sh '+service)
       return "service "+service+" closing"
    elif action == 'list':
        return str(services_list)
    elif action == 'startall':
        for service in services_list:
            thread.start_new_thread(service_start,(service,))
        return "all services starting"
    elif action == 'stopall':
        for service in services_list:
            os.system('sh ~/catkin_ws/src/cloud_v2/scripts/stop.sh '+service)
        return "all services stoping"
    else:
        return 'action error!'


if __name__ == '__main__':
    app.run('127.0.0.1', 5566)