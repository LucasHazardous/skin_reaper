from skin_reaper import SkinReaper

if __name__ == "__main__":
    r = SkinReaper()
    data = r.harvestLinks(5)
    r.setSkinPreview()
    r.collectRandom(data)
    r.kill()