# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1lll1lll_opy_
bstack11111l11_opy_ = Config.bstack1llllllll_opy_()
def bstack11l1lll11ll_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l1lll11l1_opy_(bstack11l1lll1l11_opy_, bstack11l1lll1ll1_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l1lll1l11_opy_):
        with open(bstack11l1lll1l11_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l1lll11ll_opy_(bstack11l1lll1l11_opy_):
        pac = get_pac(url=bstack11l1lll1l11_opy_)
    else:
        raise Exception(bstack1ll1ll1_opy_ (u"ࠨࡒࡤࡧࠥ࡬ࡩ࡭ࡧࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠾ࠥࢁࡽࠨ᝔").format(bstack11l1lll1l11_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack1ll1ll1_opy_ (u"ࠤ࠻࠲࠽࠴࠸࠯࠺ࠥ᝕"), 80))
        bstack11l1llll111_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l1llll111_opy_ = bstack1ll1ll1_opy_ (u"ࠪ࠴࠳࠶࠮࠱࠰࠳ࠫ᝖")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l1lll1ll1_opy_, bstack11l1llll111_opy_)
    return proxy_url
def bstack11lll11lll_opy_(config):
    return bstack1ll1ll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧ᝗") in config or bstack1ll1ll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ᝘") in config
def bstack1ll1l1ll1_opy_(config):
    if not bstack11lll11lll_opy_(config):
        return
    if config.get(bstack1ll1ll1_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ᝙")):
        return config.get(bstack1ll1ll1_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪ᝚"))
    if config.get(bstack1ll1ll1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ᝛")):
        return config.get(bstack1ll1ll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭᝜"))
def bstack111ll1111l_opy_(config, bstack11l1lll1ll1_opy_):
    proxy = bstack1ll1l1ll1_opy_(config)
    proxies = {}
    if config.get(bstack1ll1ll1_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭᝝")) or config.get(bstack1ll1ll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨ᝞")):
        if proxy.endswith(bstack1ll1ll1_opy_ (u"ࠬ࠴ࡰࡢࡥࠪ᝟")):
            proxies = bstack1l1111111l_opy_(proxy, bstack11l1lll1ll1_opy_)
        else:
            proxies = {
                bstack1ll1ll1_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬᝠ"): proxy
            }
    bstack11111l11_opy_.set_property(bstack1ll1ll1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡙ࡥࡵࡶ࡬ࡲ࡬ࡹࠧᝡ"), proxies)
    return proxies
def bstack1l1111111l_opy_(bstack11l1lll1l11_opy_, bstack11l1lll1ll1_opy_):
    proxies = {}
    global bstack11l1lll1l1l_opy_
    if bstack1ll1ll1_opy_ (u"ࠨࡒࡄࡇࡤࡖࡒࡐ࡚࡜ࠫᝢ") in globals():
        return bstack11l1lll1l1l_opy_
    try:
        proxy = bstack11l1lll11l1_opy_(bstack11l1lll1l11_opy_, bstack11l1lll1ll1_opy_)
        if bstack1ll1ll1_opy_ (u"ࠤࡇࡍࡗࡋࡃࡕࠤᝣ") in proxy:
            proxies = {}
        elif bstack1ll1ll1_opy_ (u"ࠥࡌ࡙࡚ࡐࠣᝤ") in proxy or bstack1ll1ll1_opy_ (u"ࠦࡍ࡚ࡔࡑࡕࠥᝥ") in proxy or bstack1ll1ll1_opy_ (u"࡙ࠧࡏࡄࡍࡖࠦᝦ") in proxy:
            bstack11l1lll111l_opy_ = proxy.split(bstack1ll1ll1_opy_ (u"ࠨࠠࠣᝧ"))
            if bstack1ll1ll1_opy_ (u"ࠢ࠻࠱࠲ࠦᝨ") in bstack1ll1ll1_opy_ (u"ࠣࠤᝩ").join(bstack11l1lll111l_opy_[1:]):
                proxies = {
                    bstack1ll1ll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᝪ"): bstack1ll1ll1_opy_ (u"ࠥࠦᝫ").join(bstack11l1lll111l_opy_[1:])
                }
            else:
                proxies = {
                    bstack1ll1ll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᝬ"): str(bstack11l1lll111l_opy_[0]).lower() + bstack1ll1ll1_opy_ (u"ࠧࡀ࠯࠰ࠤ᝭") + bstack1ll1ll1_opy_ (u"ࠨࠢᝮ").join(bstack11l1lll111l_opy_[1:])
                }
        elif bstack1ll1ll1_opy_ (u"ࠢࡑࡔࡒ࡜࡞ࠨᝯ") in proxy:
            bstack11l1lll111l_opy_ = proxy.split(bstack1ll1ll1_opy_ (u"ࠣࠢࠥᝰ"))
            if bstack1ll1ll1_opy_ (u"ࠤ࠽࠳࠴ࠨ᝱") in bstack1ll1ll1_opy_ (u"ࠥࠦᝲ").join(bstack11l1lll111l_opy_[1:]):
                proxies = {
                    bstack1ll1ll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᝳ"): bstack1ll1ll1_opy_ (u"ࠧࠨ᝴").join(bstack11l1lll111l_opy_[1:])
                }
            else:
                proxies = {
                    bstack1ll1ll1_opy_ (u"࠭ࡨࡵࡶࡳࡷࠬ᝵"): bstack1ll1ll1_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣ᝶") + bstack1ll1ll1_opy_ (u"ࠣࠤ᝷").join(bstack11l1lll111l_opy_[1:])
                }
        else:
            proxies = {
                bstack1ll1ll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨ᝸"): proxy
            }
    except Exception as e:
        print(bstack1ll1ll1_opy_ (u"ࠥࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠢ᝹"), bstack11l1lll1lll_opy_.format(bstack11l1lll1l11_opy_, str(e)))
    bstack11l1lll1l1l_opy_ = proxies
    return proxies