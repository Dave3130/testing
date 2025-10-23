# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1lll111l_opy_
bstack11111lll_opy_ = Config.bstack111l111l_opy_()
def bstack11l1lll1111_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l1lll11l1_opy_(bstack11l1lll1l11_opy_, bstack11l1lll11ll_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l1lll1l11_opy_):
        with open(bstack11l1lll1l11_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l1lll1111_opy_(bstack11l1lll1l11_opy_):
        pac = get_pac(url=bstack11l1lll1l11_opy_)
    else:
        raise Exception(bstack111111l_opy_ (u"ࠩࡓࡥࡨࠦࡦࡪ࡮ࡨࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸ࠿ࠦࡻࡾࠩᝇ").format(bstack11l1lll1l11_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack111111l_opy_ (u"ࠥ࠼࠳࠾࠮࠹࠰࠻ࠦᝈ"), 80))
        bstack11l1ll1llll_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l1ll1llll_opy_ = bstack111111l_opy_ (u"ࠫ࠵࠴࠰࠯࠲࠱࠴ࠬᝉ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l1lll11ll_opy_, bstack11l1ll1llll_opy_)
    return proxy_url
def bstack1l1111ll1l_opy_(config):
    return bstack111111l_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨᝊ") in config or bstack111111l_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪᝋ") in config
def bstack1l1l1lllll_opy_(config):
    if not bstack1l1111ll1l_opy_(config):
        return
    if config.get(bstack111111l_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᝌ")):
        return config.get(bstack111111l_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᝍ"))
    if config.get(bstack111111l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ᝎ")):
        return config.get(bstack111111l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧᝏ"))
def bstack1l111111ll_opy_(config, bstack11l1lll11ll_opy_):
    proxy = bstack1l1l1lllll_opy_(config)
    proxies = {}
    if config.get(bstack111111l_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᝐ")) or config.get(bstack111111l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᝑ")):
        if proxy.endswith(bstack111111l_opy_ (u"࠭࠮ࡱࡣࡦࠫᝒ")):
            proxies = bstack1111llll11_opy_(proxy, bstack11l1lll11ll_opy_)
        else:
            proxies = {
                bstack111111l_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᝓ"): proxy
            }
    bstack11111lll_opy_.set_property(bstack111111l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡓࡦࡶࡷ࡭ࡳ࡭ࡳࠨ᝔"), proxies)
    return proxies
def bstack1111llll11_opy_(bstack11l1lll1l11_opy_, bstack11l1lll11ll_opy_):
    proxies = {}
    global bstack11l1lll1l1l_opy_
    if bstack111111l_opy_ (u"ࠩࡓࡅࡈࡥࡐࡓࡑ࡛࡝ࠬ᝕") in globals():
        return bstack11l1lll1l1l_opy_
    try:
        proxy = bstack11l1lll11l1_opy_(bstack11l1lll1l11_opy_, bstack11l1lll11ll_opy_)
        if bstack111111l_opy_ (u"ࠥࡈࡎࡘࡅࡄࡖࠥ᝖") in proxy:
            proxies = {}
        elif bstack111111l_opy_ (u"ࠦࡍ࡚ࡔࡑࠤ᝗") in proxy or bstack111111l_opy_ (u"ࠧࡎࡔࡕࡒࡖࠦ᝘") in proxy or bstack111111l_opy_ (u"ࠨࡓࡐࡅࡎࡗࠧ᝙") in proxy:
            bstack11l1lll1ll1_opy_ = proxy.split(bstack111111l_opy_ (u"ࠢࠡࠤ᝚"))
            if bstack111111l_opy_ (u"ࠣ࠼࠲࠳ࠧ᝛") in bstack111111l_opy_ (u"ࠤࠥ᝜").join(bstack11l1lll1ll1_opy_[1:]):
                proxies = {
                    bstack111111l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩ᝝"): bstack111111l_opy_ (u"ࠦࠧ᝞").join(bstack11l1lll1ll1_opy_[1:])
                }
            else:
                proxies = {
                    bstack111111l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫ᝟"): str(bstack11l1lll1ll1_opy_[0]).lower() + bstack111111l_opy_ (u"ࠨ࠺࠰࠱ࠥᝠ") + bstack111111l_opy_ (u"ࠢࠣᝡ").join(bstack11l1lll1ll1_opy_[1:])
                }
        elif bstack111111l_opy_ (u"ࠣࡒࡕࡓ࡝࡟ࠢᝢ") in proxy:
            bstack11l1lll1ll1_opy_ = proxy.split(bstack111111l_opy_ (u"ࠤࠣࠦᝣ"))
            if bstack111111l_opy_ (u"ࠥ࠾࠴࠵ࠢᝤ") in bstack111111l_opy_ (u"ࠦࠧᝥ").join(bstack11l1lll1ll1_opy_[1:]):
                proxies = {
                    bstack111111l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᝦ"): bstack111111l_opy_ (u"ࠨࠢᝧ").join(bstack11l1lll1ll1_opy_[1:])
                }
            else:
                proxies = {
                    bstack111111l_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᝨ"): bstack111111l_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤᝩ") + bstack111111l_opy_ (u"ࠤࠥᝪ").join(bstack11l1lll1ll1_opy_[1:])
                }
        else:
            proxies = {
                bstack111111l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩᝫ"): proxy
            }
    except Exception as e:
        print(bstack111111l_opy_ (u"ࠦࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠣᝬ"), bstack11l1lll111l_opy_.format(bstack11l1lll1l11_opy_, str(e)))
    bstack11l1lll1l1l_opy_ = proxies
    return proxies