import openstack


def create_connection(auth_url, region, project_name, username, password, user_domain):
    return openstack.connect(
        auth_url=auth_url,
        project_name=project_name,
        username=username,
        password=password,
        region_name=region,
        user_domain_name=user_domain,
        app_name='ht_app',
        app_version='1.0',
    )


conn = create_connection(
    auth_url="https://osk.99bill.net:5000/",
    project_name="admin",
    username="admin",
    password="xfMQ2I7PoQJeU0lT10cHYuK7pg10VsN3PVK9HzBj",
    region="RegionOne",
    user_domain="Default"
)

# 查看安全组规则
# res = conn.network.security_group_rules()
# for i in res:
#     print(i.to_dict())

# 查询服务器
# for server in conn.compute.servers():
#     print(server.to_dict())

# 查看资源
# res = conn.placement.resource_classes()
# for p in res:
#     print(p.to_dict())

# 查az域
# res = conn.network.availability_zones()
# for a in res:
#     print(a.to_dict())

# res = conn.network.address_scopes()
# for a in res:
#     print(a)


# res = conn.network.pools()
# for p in res:
#     print(p.to_dict())

# 创建地址池
# attrs = {
#     "description": "ht test pool",
#     "name": "ht_pool",
#     "project_id": "66222edb77d840c9ac99ce31f527c309",
#     "subnet_id": "0e377408-34a0-4b3c-b6ac-8900d7036d4d"
# }
#
# conn.network.create_pool(**attrs)

# 地址范围
# res = conn.network.address_scopes()
# for a in res:
#     print(a.to_dict())

# RABC相关
# res = conn.network.rbac_policies()
# for r in res:
#     print(r.to_dict())

# 创建RBAC
# attrs = {
#     "object_id": "10516201-ee38-4ede-8b8b-1c35934e4172",
#     "target_tenant": "test1",
#     "project_id": "33b80c8cf0c54beba486e0a17bc033da",
#     "object_type": "network",
#     "action": "access_as_shared"
# }
#
# res = conn.network.create_rbac_policy(**attrs)
# print(res.to_dict())

# 删除RBAC
# res = conn.network.delete_rbac_policy("946bf54a-35fc-4663-ab20-09797850b925", ignore_missing=True)
# print(res.to_dict())

# 更新RBAC
# attrs = {
#     "target_tenant": "*",
# }
# res = conn.network.update_rbac_policy("315de6ff-d6eb-4465-b2a4-4cc9c2f1e7d2", **attrs)
# print(res.to_dict())

# 创建pools
# attrs = {
#     "name": "test_pool",
#     "project_id": "33b80c8cf0c54beba486e0a17bc033da",
#     "protocol": "TCP",
#     "protocol_port": 80
# }
#
# res = conn.network.create_pool(**attrs)
# print(res.to_dict())

# listeners
res = conn.network.listeners()
for l in res:
    print(l.to_dict())

# # 创建listener
# attrs = {
#     "name": "listener",
#     "project_id": "33b80c8cf0c54beba486e0a17bc033da",
#     "protocol": "TCP",
#     "protocol_port": 80
# }
#
# res = conn.network.create_listener(**attrs)
# print(res.to_dict())

# load_balancers
# res = conn.network.load_balancers()
# for l in res:
#     print(l.to_dict())

# 创建load_balancer
# attrs = {
#     "description": "test_balancer",
#     "name": "test_balancer"
# }
# res = conn.network.create_load_balancer(**attrs)
# for l in res:
#     print(l.to_dict())

# 自动拓扑
# res = conn.network.get_auto_allocated_topology()
# for t in res:
#     print(t.to_dict())
