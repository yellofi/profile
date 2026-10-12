import concurrent.futures,hashlib,json,subprocess
from pathlib import Path
ORIGIN="https://yunseob-profile-preview.brinyseal32.chatgpt.site"
ROOT=Path(__file__).resolve().parent.parent
entries=json.loads((ROOT/"scripts/assets-manifest.json").read_text())
def fetch(entry):
    target=ROOT/entry["path"]
    if target.is_file() and hashlib.sha256(target.read_bytes()).hexdigest()==entry["sha256"]:
        return
    target.parent.mkdir(parents=True,exist_ok=True)
    temporary=target.with_suffix(target.suffix+".tmp")
    for attempt in range(3):
        subprocess.run(["curl","--fail","--silent","--show-error","--location","--retry","3","--retry-all-errors","--connect-timeout","20","--max-time","120","--output",str(temporary),ORIGIN+"/"+entry["path"]],check=True)
        if hashlib.sha256(temporary.read_bytes()).hexdigest()==entry["sha256"]:
            temporary.replace(target)
            return
    raise RuntimeError("Asset checksum mismatch: "+entry["path"])
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    list(pool.map(fetch,entries))
for target in [ROOT/"index.html",*(ROOT/"seminars").glob("*.html")]:
    source=target.read_text()
    prefix="../" if target.parent.name=="seminars" else ""
    source=source.replace(ORIGIN+"/assets/",prefix+"assets/")
    source=source.replace(ORIGIN+"/","https://yellofi.github.io/profile/")
    target.write_text(source)
(ROOT/".nojekyll").touch()
print(f"Verified {len(entries)} local assets and removed temporary hosting references.")
