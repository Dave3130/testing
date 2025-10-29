# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1ll111l1_opy_
bstack1lll11111_opy_ = Config.bstack1llll111l_opy_()
def bstack11l1ll11lll_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l1ll11ll1_opy_(bstack11l1ll11l11_opy_, bstack11l1ll111ll_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l1ll11l11_opy_):
        with open(bstack11l1ll11l11_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l1ll11lll_opy_(bstack11l1ll11l11_opy_):
        pac = get_pac(url=bstack11l1ll11l11_opy_)
    else:
        raise Exception(bstack11l11ll_opy_ (u"ࠫࡕࡧࡣࠡࡨ࡬ࡰࡪࠦࡤࡰࡧࡶࠤࡳࡵࡴࠡࡧࡻ࡭ࡸࡺ࠺ࠡࡽࢀࠫខ").format(bstack11l1ll11l11_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack11l11ll_opy_ (u"ࠧ࠾࠮࠹࠰࠻࠲࠽ࠨគ"), 80))
        bstack11l1ll11l1l_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l1ll11l1l_opy_ = bstack11l11ll_opy_ (u"࠭࠰࠯࠲࠱࠴࠳࠶ࠧឃ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l1ll111ll_opy_, bstack11l1ll11l1l_opy_)
    return proxy_url
def bstack1l111l11ll_opy_(config):
    return bstack11l11ll_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪង") in config or bstack11l11ll_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬច") in config
def bstack1l11ll111l_opy_(config):
    if not bstack1l111l11ll_opy_(config):
        return
    if config.get(bstack11l11ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬឆ")):
        return config.get(bstack11l11ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ជ"))
    if config.get(bstack11l11ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨឈ")):
        return config.get(bstack11l11ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩញ"))
def bstack1l1ll111ll_opy_(config, bstack11l1ll111ll_opy_):
    proxy = bstack1l11ll111l_opy_(config)
    proxies = {}
    if config.get(bstack11l11ll_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩដ")) or config.get(bstack11l11ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫឋ")):
        if proxy.endswith(bstack11l11ll_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭ឌ")):
            proxies = bstack111ll1ll1_opy_(proxy, bstack11l1ll111ll_opy_)
        else:
            proxies = {
                bstack11l11ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨឍ"): proxy
            }
    bstack1lll11111_opy_.set_property(bstack11l11ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡕࡨࡸࡹ࡯࡮ࡨࡵࠪណ"), proxies)
    return proxies
def bstack111ll1ll1_opy_(bstack11l1ll11l11_opy_, bstack11l1ll111ll_opy_):
    proxies = {}
    global bstack11l1ll1l11l_opy_
    if bstack11l11ll_opy_ (u"ࠫࡕࡇࡃࡠࡒࡕࡓ࡝࡟ࠧត") in globals():
        return bstack11l1ll1l11l_opy_
    try:
        proxy = bstack11l1ll11ll1_opy_(bstack11l1ll11l11_opy_, bstack11l1ll111ll_opy_)
        if bstack11l11ll_opy_ (u"ࠧࡊࡉࡓࡇࡆࡘࠧថ") in proxy:
            proxies = {}
        elif bstack11l11ll_opy_ (u"ࠨࡈࡕࡖࡓࠦទ") in proxy or bstack11l11ll_opy_ (u"ࠢࡉࡖࡗࡔࡘࠨធ") in proxy or bstack11l11ll_opy_ (u"ࠣࡕࡒࡇࡐ࡙ࠢន") in proxy:
            bstack11l1ll1l111_opy_ = proxy.split(bstack11l11ll_opy_ (u"ࠤࠣࠦប"))
            if bstack11l11ll_opy_ (u"ࠥ࠾࠴࠵ࠢផ") in bstack11l11ll_opy_ (u"ࠦࠧព").join(bstack11l1ll1l111_opy_[1:]):
                proxies = {
                    bstack11l11ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫភ"): bstack11l11ll_opy_ (u"ࠨࠢម").join(bstack11l1ll1l111_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l11ll_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭យ"): str(bstack11l1ll1l111_opy_[0]).lower() + bstack11l11ll_opy_ (u"ࠣ࠼࠲࠳ࠧរ") + bstack11l11ll_opy_ (u"ࠤࠥល").join(bstack11l1ll1l111_opy_[1:])
                }
        elif bstack11l11ll_opy_ (u"ࠥࡔࡗࡕࡘ࡚ࠤវ") in proxy:
            bstack11l1ll1l111_opy_ = proxy.split(bstack11l11ll_opy_ (u"ࠦࠥࠨឝ"))
            if bstack11l11ll_opy_ (u"ࠧࡀ࠯࠰ࠤឞ") in bstack11l11ll_opy_ (u"ࠨࠢស").join(bstack11l1ll1l111_opy_[1:]):
                proxies = {
                    bstack11l11ll_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ហ"): bstack11l11ll_opy_ (u"ࠣࠤឡ").join(bstack11l1ll1l111_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l11ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨអ"): bstack11l11ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦឣ") + bstack11l11ll_opy_ (u"ࠦࠧឤ").join(bstack11l1ll1l111_opy_[1:])
                }
        else:
            proxies = {
                bstack11l11ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫឥ"): proxy
            }
    except Exception as e:
        print(bstack11l11ll_opy_ (u"ࠨࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠥឦ"), bstack11l1ll111l1_opy_.format(bstack11l1ll11l11_opy_, str(e)))
    bstack11l1ll1l11l_opy_ = proxies
    return proxies