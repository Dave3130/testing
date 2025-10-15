# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1lll1111_opy_
bstack111111ll_opy_ = Config.bstack111l1ll1_opy_()
def bstack11l1lll1l1l_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l1lll11l1_opy_(bstack11l1lll1ll1_opy_, bstack11l1lll11ll_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l1lll1ll1_opy_):
        with open(bstack11l1lll1ll1_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l1lll1l1l_opy_(bstack11l1lll1ll1_opy_):
        pac = get_pac(url=bstack11l1lll1ll1_opy_)
    else:
        raise Exception(bstack1ll1l_opy_ (u"ࠧࡑࡣࡦࠤ࡫࡯࡬ࡦࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡪࡾࡩࡴࡶ࠽ࠤࢀࢃࠧᝌ").format(bstack11l1lll1ll1_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack1ll1l_opy_ (u"ࠣ࠺࠱࠼࠳࠾࠮࠹ࠤᝍ"), 80))
        bstack11l1ll1llll_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l1ll1llll_opy_ = bstack1ll1l_opy_ (u"ࠩ࠳࠲࠵࠴࠰࠯࠲ࠪᝎ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l1lll11ll_opy_, bstack11l1ll1llll_opy_)
    return proxy_url
def bstack1l1llll111_opy_(config):
    return bstack1ll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ᝏ") in config or bstack1ll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨᝐ") in config
def bstack1l111l11l_opy_(config):
    if not bstack1l1llll111_opy_(config):
        return
    if config.get(bstack1ll1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨᝑ")):
        return config.get(bstack1ll1l_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩᝒ"))
    if config.get(bstack1ll1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᝓ")):
        return config.get(bstack1ll1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ᝔"))
def bstack111l1l1ll_opy_(config, bstack11l1lll11ll_opy_):
    proxy = bstack1l111l11l_opy_(config)
    proxies = {}
    if config.get(bstack1ll1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ᝕")) or config.get(bstack1ll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧ᝖")):
        if proxy.endswith(bstack1ll1l_opy_ (u"ࠫ࠳ࡶࡡࡤࠩ᝗")):
            proxies = bstack11l1l1l1l1_opy_(proxy, bstack11l1lll11ll_opy_)
        else:
            proxies = {
                bstack1ll1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫ᝘"): proxy
            }
    bstack111111ll_opy_.set_property(bstack1ll1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭᝙"), proxies)
    return proxies
def bstack11l1l1l1l1_opy_(bstack11l1lll1ll1_opy_, bstack11l1lll11ll_opy_):
    proxies = {}
    global bstack11l1lll1l11_opy_
    if bstack1ll1l_opy_ (u"ࠧࡑࡃࡆࡣࡕࡘࡏ࡙࡛ࠪ᝚") in globals():
        return bstack11l1lll1l11_opy_
    try:
        proxy = bstack11l1lll11l1_opy_(bstack11l1lll1ll1_opy_, bstack11l1lll11ll_opy_)
        if bstack1ll1l_opy_ (u"ࠣࡆࡌࡖࡊࡉࡔࠣ᝛") in proxy:
            proxies = {}
        elif bstack1ll1l_opy_ (u"ࠤࡋࡘ࡙ࡖࠢ᝜") in proxy or bstack1ll1l_opy_ (u"ࠥࡌ࡙࡚ࡐࡔࠤ᝝") in proxy or bstack1ll1l_opy_ (u"ࠦࡘࡕࡃࡌࡕࠥ᝞") in proxy:
            bstack11l1lll111l_opy_ = proxy.split(bstack1ll1l_opy_ (u"ࠧࠦࠢ᝟"))
            if bstack1ll1l_opy_ (u"ࠨ࠺࠰࠱ࠥᝠ") in bstack1ll1l_opy_ (u"ࠢࠣᝡ").join(bstack11l1lll111l_opy_[1:]):
                proxies = {
                    bstack1ll1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᝢ"): bstack1ll1l_opy_ (u"ࠤࠥᝣ").join(bstack11l1lll111l_opy_[1:])
                }
            else:
                proxies = {
                    bstack1ll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩᝤ"): str(bstack11l1lll111l_opy_[0]).lower() + bstack1ll1l_opy_ (u"ࠦ࠿࠵࠯ࠣᝥ") + bstack1ll1l_opy_ (u"ࠧࠨᝦ").join(bstack11l1lll111l_opy_[1:])
                }
        elif bstack1ll1l_opy_ (u"ࠨࡐࡓࡑ࡛࡝ࠧᝧ") in proxy:
            bstack11l1lll111l_opy_ = proxy.split(bstack1ll1l_opy_ (u"ࠢࠡࠤᝨ"))
            if bstack1ll1l_opy_ (u"ࠣ࠼࠲࠳ࠧᝩ") in bstack1ll1l_opy_ (u"ࠤࠥᝪ").join(bstack11l1lll111l_opy_[1:]):
                proxies = {
                    bstack1ll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩᝫ"): bstack1ll1l_opy_ (u"ࠦࠧᝬ").join(bstack11l1lll111l_opy_[1:])
                }
            else:
                proxies = {
                    bstack1ll1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫ᝭"): bstack1ll1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢᝮ") + bstack1ll1l_opy_ (u"ࠢࠣᝯ").join(bstack11l1lll111l_opy_[1:])
                }
        else:
            proxies = {
                bstack1ll1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧᝰ"): proxy
            }
    except Exception as e:
        print(bstack1ll1l_opy_ (u"ࠤࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷࠨ᝱"), bstack11l1lll1111_opy_.format(bstack11l1lll1ll1_opy_, str(e)))
    bstack11l1lll1l11_opy_ = proxies
    return proxies