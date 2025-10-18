# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1lll11l1_opy_
bstack1111111l_opy_ = Config.bstack11l11l1l_opy_()
def bstack11l1lll1l1l_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l1lll11ll_opy_(bstack11l1lll1l11_opy_, bstack11l1ll1llll_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l1lll1l11_opy_):
        with open(bstack11l1lll1l11_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l1lll1l1l_opy_(bstack11l1lll1l11_opy_):
        pac = get_pac(url=bstack11l1lll1l11_opy_)
    else:
        raise Exception(bstack1l1lll1_opy_ (u"ࠨࡒࡤࡧࠥ࡬ࡩ࡭ࡧࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠾ࠥࢁࡽࠨᝍ").format(bstack11l1lll1l11_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack1l1lll1_opy_ (u"ࠤ࠻࠲࠽࠴࠸࠯࠺ࠥᝎ"), 80))
        bstack11l1lll1111_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l1lll1111_opy_ = bstack1l1lll1_opy_ (u"ࠪ࠴࠳࠶࠮࠱࠰࠳ࠫᝏ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l1ll1llll_opy_, bstack11l1lll1111_opy_)
    return proxy_url
def bstack1lll11lll1_opy_(config):
    return bstack1l1lll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᝐ") in config or bstack1l1lll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᝑ") in config
def bstack11lll11ll_opy_(config):
    if not bstack1lll11lll1_opy_(config):
        return
    if config.get(bstack1l1lll1_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩᝒ")):
        return config.get(bstack1l1lll1_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᝓ"))
    if config.get(bstack1l1lll1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ᝔")):
        return config.get(bstack1l1lll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭᝕"))
def bstack11l1l11ll_opy_(config, bstack11l1ll1llll_opy_):
    proxy = bstack11lll11ll_opy_(config)
    proxies = {}
    if config.get(bstack1l1lll1_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭᝖")) or config.get(bstack1l1lll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨ᝗")):
        if proxy.endswith(bstack1l1lll1_opy_ (u"ࠬ࠴ࡰࡢࡥࠪ᝘")):
            proxies = bstack11l111llll_opy_(proxy, bstack11l1ll1llll_opy_)
        else:
            proxies = {
                bstack1l1lll1_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬ᝙"): proxy
            }
    bstack1111111l_opy_.set_property(bstack1l1lll1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹࠧ᝚"), proxies)
    return proxies
def bstack11l111llll_opy_(bstack11l1lll1l11_opy_, bstack11l1ll1llll_opy_):
    proxies = {}
    global bstack11l1lll111l_opy_
    if bstack1l1lll1_opy_ (u"ࠨࡒࡄࡇࡤࡖࡒࡐ࡚࡜ࠫ᝛") in globals():
        return bstack11l1lll111l_opy_
    try:
        proxy = bstack11l1lll11ll_opy_(bstack11l1lll1l11_opy_, bstack11l1ll1llll_opy_)
        if bstack1l1lll1_opy_ (u"ࠤࡇࡍࡗࡋࡃࡕࠤ᝜") in proxy:
            proxies = {}
        elif bstack1l1lll1_opy_ (u"ࠥࡌ࡙࡚ࡐࠣ᝝") in proxy or bstack1l1lll1_opy_ (u"ࠦࡍ࡚ࡔࡑࡕࠥ᝞") in proxy or bstack1l1lll1_opy_ (u"࡙ࠧࡏࡄࡍࡖࠦ᝟") in proxy:
            bstack11l1ll1lll1_opy_ = proxy.split(bstack1l1lll1_opy_ (u"ࠨࠠࠣᝠ"))
            if bstack1l1lll1_opy_ (u"ࠢ࠻࠱࠲ࠦᝡ") in bstack1l1lll1_opy_ (u"ࠣࠤᝢ").join(bstack11l1ll1lll1_opy_[1:]):
                proxies = {
                    bstack1l1lll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᝣ"): bstack1l1lll1_opy_ (u"ࠥࠦᝤ").join(bstack11l1ll1lll1_opy_[1:])
                }
            else:
                proxies = {
                    bstack1l1lll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᝥ"): str(bstack11l1ll1lll1_opy_[0]).lower() + bstack1l1lll1_opy_ (u"ࠧࡀ࠯࠰ࠤᝦ") + bstack1l1lll1_opy_ (u"ࠨࠢᝧ").join(bstack11l1ll1lll1_opy_[1:])
                }
        elif bstack1l1lll1_opy_ (u"ࠢࡑࡔࡒ࡜࡞ࠨᝨ") in proxy:
            bstack11l1ll1lll1_opy_ = proxy.split(bstack1l1lll1_opy_ (u"ࠣࠢࠥᝩ"))
            if bstack1l1lll1_opy_ (u"ࠤ࠽࠳࠴ࠨᝪ") in bstack1l1lll1_opy_ (u"ࠥࠦᝫ").join(bstack11l1ll1lll1_opy_[1:]):
                proxies = {
                    bstack1l1lll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᝬ"): bstack1l1lll1_opy_ (u"ࠧࠨ᝭").join(bstack11l1ll1lll1_opy_[1:])
                }
            else:
                proxies = {
                    bstack1l1lll1_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬᝮ"): bstack1l1lll1_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣᝯ") + bstack1l1lll1_opy_ (u"ࠣࠤᝰ").join(bstack11l1ll1lll1_opy_[1:])
                }
        else:
            proxies = {
                bstack1l1lll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨ᝱"): proxy
            }
    except Exception as e:
        print(bstack1l1lll1_opy_ (u"ࠥࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠢᝲ"), bstack11l1lll11l1_opy_.format(bstack11l1lll1l11_opy_, str(e)))
    bstack11l1lll111l_opy_ = proxies
    return proxies