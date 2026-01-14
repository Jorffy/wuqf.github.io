from scholarly import scholarly, ProxyGenerator
import jsonpickle
import json
from datetime import datetime
import os, time
from scholarly._proxy_generator import MaxTriesExceededException

max_attempts = 100
wait_seconds = 10  # 10 minutes

for attempt in range(1, max_attempts + 1):
    try:
        print(f"Attempt {attempt}:")
        # Setup proxy
        pg = ProxyGenerator()
        pg.FreeProxies()  # Use free rotating proxies
        scholarly.use_proxy(pg)
        
        # author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
        author: dict = scholarly.search_author_id("zo8SfrMAAAAJ")
        scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
        print(f"Attempt {attempt} success")
        break  # Exit loop on first success
    except Exception as e:
        print(f"Attempt {attempt} failed with error: {e}")
        time.sleep(wait_seconds)
else:
    print("All 100 attempts failed.")

# try:
#     print("正在查找作者信息...")
#     # Setup proxy
#     pg = ProxyGenerator()
#     pg.FreeProxies()  # Use free rotating proxies
#     scholarly.use_proxy(pg)
#     # author: dict = scholarly.search_author_id(os.environ["GOOGLE_SCHOLAR_ID"])
#     author: dict = scholarly.search_author_id("zo8SfrMAAAAJ")
# except MaxTriesExceededException as e:
#     print(f"发生异常: {e}")

print("正在填充作者详细信息...")
# scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
name = author["name"]
author["updated"] = str(datetime.now())
author["publications"] = {v["author_pub_id"]: v for v in author["publications"]}
print(json.dumps(author, indent=2))

print("正在创建结果目录...")
os.makedirs("results", exist_ok=True)

print("正在保存作者数据...")
with open(f"results/gs_data.json", "w") as outfile:
    json.dump(author, outfile, ensure_ascii=False)

print("正在生成 Shields.io 数据...")
shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author.get('citedby', 0)}",
}

print("正在保存 Shields.io 数据...")
with open(f"results/gs_data_shieldsio.json", "w") as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

print("数据处理完成。")
