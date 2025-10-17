# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1lll1111_opy_
bstack111ll111_opy_ = Config.bstack111ll1ll_opy_()
def bstack11l1lll11ll_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l1lll1l11_opy_(bstack11l1ll1lll1_opy_, bstack11l1ll1ll1l_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l1ll1lll1_opy_):
        with open(bstack11l1ll1lll1_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l1lll11ll_opy_(bstack11l1ll1lll1_opy_):
        pac = get_pac(url=bstack11l1ll1lll1_opy_)
    else:
        raise Exception(bstack11l111_opy_ (u"ࠪࡔࡦࡩࠠࡧ࡫࡯ࡩࠥࡪ࡯ࡦࡵࠣࡲࡴࡺࠠࡦࡺ࡬ࡷࡹࡀࠠࡼࡿࠪᝁ").format(bstack11l1ll1lll1_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack11l111_opy_ (u"ࠦ࠽࠴࠸࠯࠺࠱࠼ࠧᝂ"), 80))
        bstack11l1ll1llll_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l1ll1llll_opy_ = bstack11l111_opy_ (u"ࠬ࠶࠮࠱࠰࠳࠲࠵࠭ᝃ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l1ll1ll1l_opy_, bstack11l1ll1llll_opy_)
    return proxy_url
def bstack11lll111l_opy_(config):
    return bstack11l111_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩᝄ") in config or bstack11l111_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᝅ") in config
def bstack11111ll11l_opy_(config):
    if not bstack11lll111l_opy_(config):
        return
    if config.get(bstack11l111_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᝆ")):
        return config.get(bstack11l111_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᝇ"))
    if config.get(bstack11l111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧᝈ")):
        return config.get(bstack11l111_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨᝉ"))
def bstack1llllll11l_opy_(config, bstack11l1ll1ll1l_opy_):
    proxy = bstack11111ll11l_opy_(config)
    proxies = {}
    if config.get(bstack11l111_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨᝊ")) or config.get(bstack11l111_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪᝋ")):
        if proxy.endswith(bstack11l111_opy_ (u"ࠧ࠯ࡲࡤࡧࠬᝌ")):
            proxies = bstack1111111ll_opy_(proxy, bstack11l1ll1ll1l_opy_)
        else:
            proxies = {
                bstack11l111_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᝍ"): proxy
            }
    bstack111ll111_opy_.set_property(bstack11l111_opy_ (u"ࠩࡳࡶࡴࡾࡹࡔࡧࡷࡸ࡮ࡴࡧࡴࠩᝎ"), proxies)
    return proxies
def bstack1111111ll_opy_(bstack11l1ll1lll1_opy_, bstack11l1ll1ll1l_opy_):
    proxies = {}
    global bstack11l1lll111l_opy_
    if bstack11l111_opy_ (u"ࠪࡔࡆࡉ࡟ࡑࡔࡒ࡜࡞࠭ᝏ") in globals():
        return bstack11l1lll111l_opy_
    try:
        proxy = bstack11l1lll1l11_opy_(bstack11l1ll1lll1_opy_, bstack11l1ll1ll1l_opy_)
        if bstack11l111_opy_ (u"ࠦࡉࡏࡒࡆࡅࡗࠦᝐ") in proxy:
            proxies = {}
        elif bstack11l111_opy_ (u"ࠧࡎࡔࡕࡒࠥᝑ") in proxy or bstack11l111_opy_ (u"ࠨࡈࡕࡖࡓࡗࠧᝒ") in proxy or bstack11l111_opy_ (u"ࠢࡔࡑࡆࡏࡘࠨᝓ") in proxy:
            bstack11l1lll11l1_opy_ = proxy.split(bstack11l111_opy_ (u"ࠣࠢࠥ᝔"))
            if bstack11l111_opy_ (u"ࠤ࠽࠳࠴ࠨ᝕") in bstack11l111_opy_ (u"ࠥࠦ᝖").join(bstack11l1lll11l1_opy_[1:]):
                proxies = {
                    bstack11l111_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪ᝗"): bstack11l111_opy_ (u"ࠧࠨ᝘").join(bstack11l1lll11l1_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l111_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬ᝙"): str(bstack11l1lll11l1_opy_[0]).lower() + bstack11l111_opy_ (u"ࠢ࠻࠱࠲ࠦ᝚") + bstack11l111_opy_ (u"ࠣࠤ᝛").join(bstack11l1lll11l1_opy_[1:])
                }
        elif bstack11l111_opy_ (u"ࠤࡓࡖࡔ࡞࡙ࠣ᝜") in proxy:
            bstack11l1lll11l1_opy_ = proxy.split(bstack11l111_opy_ (u"ࠥࠤࠧ᝝"))
            if bstack11l111_opy_ (u"ࠦ࠿࠵࠯ࠣ᝞") in bstack11l111_opy_ (u"ࠧࠨ᝟").join(bstack11l1lll11l1_opy_[1:]):
                proxies = {
                    bstack11l111_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬᝠ"): bstack11l111_opy_ (u"ࠢࠣᝡ").join(bstack11l1lll11l1_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l111_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᝢ"): bstack11l111_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥᝣ") + bstack11l111_opy_ (u"ࠥࠦᝤ").join(bstack11l1lll11l1_opy_[1:])
                }
        else:
            proxies = {
                bstack11l111_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᝥ"): proxy
            }
    except Exception as e:
        print(bstack11l111_opy_ (u"ࠧࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠤᝦ"), bstack11l1lll1111_opy_.format(bstack11l1ll1lll1_opy_, str(e)))
    bstack11l1lll111l_opy_ = proxies
    return proxies