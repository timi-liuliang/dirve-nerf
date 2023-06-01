import libtorrent as lt

def download_torrent(torrent_path, save_path):
    # 创建 session 对象
    ses = lt.session()

    # 加载 torrent 文件
    with open(torrent_path, "rb") as f:
        e = lt.bdecode(f.read())
        info = lt.torrent_info(e)

    # 添加 torrent 到 session
    params = {'save_path': save_path, 'storage_mode': lt.storage_mode_t(2)}
    h = ses.add_torrent(params)
    h.set_torrent_info(info)

    # 下载资源
    print("Downloading ", info.name())
    while (not h.is_seed()):
        s = h.status()
        state_str = ['queued', 'checking', 'downloading metadata', \
                        'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']
        print('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
                (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
                s.num_peers, state_str[s.state]))
        time.sleep(1)

    # 关闭 session
    ses.remove_torrent(h)


download_torrent("./download/test.torrent", "./download/")