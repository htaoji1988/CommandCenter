import openstack

# Initialize and turn on debug logging
openstack.enable_logging(debug=False)

# Initialize connection
conn = openstack.connect(cloud='openstack')

# 查询服务器
# for server in conn.compute.servers():
#     print(server.to_dict())


# 查看快照
# for image in conn.compute.images():
#     print(image.to_dict())

# 查看类型模板flavor
# for flavor in conn.compute.flavors():
#     print(flavor.to_dict())

# 查看网络配置
# for network in conn.network.networks():
#     print(network.to_dict())

# 创建虚拟机
# print("Create Server:")
# image = conn.compute.find_image("centos8stream")
# flavor = conn.compute.find_flavor("m1.medium")
# network = conn.network.find_network("vlan116")
#
# server = conn.compute.create_server(
#     name="ht_test3",
#     image_id=image.id,
#     flavor_id=flavor.id,
#     networks=[{"uuid": network.id}]
# )
#
# res = conn.compute.wait_for_server(server)
# print(server.to_dict())

# 删除虚拟机
# res = conn.compute.delete_server('7eca5a3b-4433-4cb9-a67c-9ef2afb910c7')
# print(res)

# 更新虚拟机
# kwargs = {
#     "description": "我的测试机1"
# }
# res = conn.compute.update_server('6d8134fe-5a6e-4e46-9a4d-a5e09260e3eb', **kwargs)
# print(res.to_dict())

# 创建server镜像
# res = conn.compute.create_server_image('419d6d8a-e143-4b87-946f-549b9952eb85', "ht_image")
# print(res)

# 删除镜像
# res = conn.compute.delete_image("c5a8fa43-ab8d-44fa-88fc-7509b51a88a4")

# 操作server
#   start_server(server)
# 	stop_server(server)
# 	reboot_server(server, reboot_type)
# 	pause_server(server)
# 	unpause_server(server)
# res = conn.compute.reboot_server('419d6d8a-e143-4b87-946f-549b9952eb85', "SOFT")
# res = conn.compute.get_server_password('419d6d8a-e143-4b87-946f-549b9952eb85')
# res = conn.compute.reboot_server('419d6d8a-e143-4b87-946f-549b9952eb85', "SOFT")


# 查看存储
# for volume in conn.block_storage.volumes():
#     print(volume.to_dict())

# 创建volume
# volume_kwargs = {
#     "size": 2,
#     "type": "__DEFAULT__",
#     "name": "ht_volume"
# }
# res = conn.create_volume(**volume_kwargs)
# print(res)

# 删除volume
# res = conn.delete_volume('ht_volume')
# print(res)

# 创建flavor
# kwargs = {
#     "name": "ht_flavor2",
#     "ram": 2048,
#     "vcpus": 2,
#     "disk": 20
# }
# res = conn.compute.create_flavor(**kwargs)

# 获取服务
# res = conn.compute.services()

# server 的ips
# res = conn.compute.server_ips('419d6d8a-e143-4b87-946f-549b9952eb85')
# for ip in res:
#     print(ip.to_dict())

# 服务器组
# res = conn.compute.server_groups()
# for g in res:
#     print(g.to_dict())


# 从url同步镜像文件
# res = conn.image.import_image(image, method='glance-direct', uri=None, store=None, stores=None, all_stores=None, all_stores_must_succeed=None)

# 镜像二进制文件
# res = conn.image.stage_image("ht_linux", filename='e:/tmp/TinyCore-current.iso')

# 上传镜像
# res = conn.image.upload_image(container_format='ovf', disk_format='iso', data='e:/tmp/TinyCore-current.iso')

# 删除镜像
# res = conn.image.delete_image('c5a8fa43-ab8d-44fa-88fc-7509b51a88a4', ignore_missing=True)

# res = conn.image.create_image('TinyCore', filename='d:/tmp/TinyCore-current.iso')

# res = conn.image.members('10f9171d-36b0-4425-864b-d5fab6661099')
# for m in res:
#     print(m.to_dict())

# 查看卷快照
# res = conn.block_storage.snapshots()
# for s in res:
#     print(s.to_dict())

# 创建卷快照
# attrs = {
#     "volume_id": "105ce497-3c6b-4771-a748-e5797fbbb067",
#     "name": "ht_volume_snapshot"
# }
# res = conn.block_storage.create_snapshot(**attrs)
#
# print(res.to_dict())

# 网络
# res = conn.network.dhcp_agent_hosting_networks(agent, **query)

# 创建网络
# attrs = {
#     "description": "测试网络",
#     "name": "ht_net",
#     "project_id": "66222edb77d840c9ac99ce31f527c309",
#     "provider_network_type": "vlan"
# }
#
# res = conn.network.create_network(**attrs)
# print(res.to_dict())

# attrs = {
#     "name": "ht_net2"
# }
#
# res = conn.network.update_network("10516201-ee38-4ede-8b8b-1c35934e4172", **attrs)
# print(res.to_dict())

# 创建子网
# attrs = {
#     "ip_version": 4,
#     "cidr": "192.168.117.0/24",
#     "name": "117subnet",
#     "gateway_ip": "192.168.117.1",
#     "network_id": "10516201-ee38-4ede-8b8b-1c35934e4172"
# }
# res = conn.network.create_subnet(**attrs)
# print(res.to_dict())

# 查看子网
# res = conn.network.subnets()
# for s in res:
#     print(s.to_dict())

# 更新子网
# attrs = {
#     "name": "ht_net2"
# }
# res = conn.network.update_subnet("0e377408-34a0-4b3c-b6ac-8900d7036d4d", **attrs)
# print(res.to_dict())

# 查询路由
# res = conn.network.routers()
# for r in res:
#     print(r.to_dict())

# 创建路由
# attrs = {
#     "name": "ht-router",
# }
#
# res = conn.network.create_router(**attrs)
# print(res.to_dict())

# res = conn.network.create_router(**attrs)
# print(res.to_dict())
#     "name": "ht-router",
# }

# 打开一个端口
# attrs = {
#     "network_id": "10516201-ee38-4ede-8b8b-1c35934e4172",
#     "name": "ht_test_port",
# }

# res = conn.network.create_security_group(name='ht-test-security-group')
# print(res.to_dict())


# 打开端口和协议
# attrs = {
#     "security_group_id": "baa2b8d2-9a8d-4d00-b21a-7714125b13ed",
#     "direction": 'ingress',
#     "remote_ip_prefix": '0.0.0.0/0',
#     "protocol": 'tcp',
#     "port_range_max": '443',
#     "port_range_min": '443',
#     "ethertype": 'IPv4'
# }
#
# res = conn.network.create_security_group_rule(**attrs)
# print(res.to_dict())

# for zone in conn.dns.zones():
#     print(zone)


# res = conn.compute.hypervisors()
# for h in res:
#     print(h.to_dict())

# res = conn.image.get_image_schema()
# print(res.to_dict())

# 绑定volume

# attrs = {
#     "volumeId": "105ce497-3c6b-4771-a748-e5797fbbb067"
# }
#
# res = conn.compute.create_volume_attachment("419d6d8a-e143-4b87-946f-549b9952eb85", **attrs)
# print(res.to_dict())

# 查看挂载信息
# res = conn.compute.volume_attachments("419d6d8a-e143-4b87-946f-549b9952eb85")
#
# for i in res:
#     print(i.to_dict())

# 安全组
# res = conn.network.security_groups()
# for s in res:
#     print(s.to_dict())

# 创建安全组
# attrs = {
#     "name": "测试安全组",
#     "description": "测试安全组",
#     "project_id": "66222edb77d840c9ac99ce31f527c309"
# }
# res = conn.network.create_security_group(**attrs)
# print(res.to_dict())

# 查看安全组规则
# res = conn.network.security_group_rules()
# for i in res:
#     print(i.to_dict())

# 创建安全组规则
# attrs = {
#     "direction": "ingress",  # ingress进 or egress出
#     "protocol": "tcp",
#     "port_range_max": "8080",
#     "port_range_min": "8080",
#     'remote_ip_prefix': '0.0.0.0/0',
#     "security_group_id": "7f24d77f-de89-4c44-a1de-2a0a89f7db29"
# }
# res = conn.network.create_security_group_rule(**attrs)
# print(res.to_dict())


# attrs = {
#     "volumeId": "105ce497-3c6b-4771-a748-e5797fbbb067"
# }
#
# conn.compute.create_volume_attachment("6d8134fe-5a6e-4e46-9a4d-a5e09260e3eb", **attrs)

# res = conn.network.pools()
# for p in res:
#     print(p.to_dict())
