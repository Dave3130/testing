# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1ll1111l_opy_
bstack1llllll1l_opy_ = Config.bstack1lll11ll1_opy_()
def bstack11l1l1lllll_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l1l1lll1l_opy_(bstack11l1ll111l1_opy_, bstack11l1ll111ll_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l1ll111l1_opy_):
        with open(bstack11l1ll111l1_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l1l1lllll_opy_(bstack11l1ll111l1_opy_):
        pac = get_pac(url=bstack11l1ll111l1_opy_)
    else:
        raise Exception(bstack11ll1ll_opy_ (u"࠭ࡐࡢࡥࠣࡪ࡮ࡲࡥࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠼ࠣࡿࢂ࠭ទ").format(bstack11l1ll111l1_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack11ll1ll_opy_ (u"ࠢ࠹࠰࠻࠲࠽࠴࠸ࠣធ"), 80))
        bstack11l1ll11l11_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l1ll11l11_opy_ = bstack11ll1ll_opy_ (u"ࠨ࠲࠱࠴࠳࠶࠮࠱ࠩន")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l1ll111ll_opy_, bstack11l1ll11l11_opy_)
    return proxy_url
def bstack1111lllll_opy_(config):
    return bstack11ll1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬប") in config or bstack11ll1ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧផ") in config
def bstack1l111ll1ll_opy_(config):
    if not bstack1111lllll_opy_(config):
        return
    if config.get(bstack11ll1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧព")):
        return config.get(bstack11ll1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨភ"))
    if config.get(bstack11ll1ll_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪម")):
        return config.get(bstack11ll1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫយ"))
def bstack11l111l11_opy_(config, bstack11l1ll111ll_opy_):
    proxy = bstack1l111ll1ll_opy_(config)
    proxies = {}
    if config.get(bstack11ll1ll_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫរ")) or config.get(bstack11ll1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ល")):
        if proxy.endswith(bstack11ll1ll_opy_ (u"ࠪ࠲ࡵࡧࡣࠨវ")):
            proxies = bstack1l11l1l111_opy_(proxy, bstack11l1ll111ll_opy_)
        else:
            proxies = {
                bstack11ll1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪឝ"): proxy
            }
    bstack1llllll1l_opy_.set_property(bstack11ll1ll_opy_ (u"ࠬࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠬឞ"), proxies)
    return proxies
def bstack1l11l1l111_opy_(bstack11l1ll111l1_opy_, bstack11l1ll111ll_opy_):
    proxies = {}
    global bstack11l1l1llll1_opy_
    if bstack11ll1ll_opy_ (u"࠭ࡐࡂࡅࡢࡔࡗࡕࡘ࡚ࠩស") in globals():
        return bstack11l1l1llll1_opy_
    try:
        proxy = bstack11l1l1lll1l_opy_(bstack11l1ll111l1_opy_, bstack11l1ll111ll_opy_)
        if bstack11ll1ll_opy_ (u"ࠢࡅࡋࡕࡉࡈ࡚ࠢហ") in proxy:
            proxies = {}
        elif bstack11ll1ll_opy_ (u"ࠣࡊࡗࡘࡕࠨឡ") in proxy or bstack11ll1ll_opy_ (u"ࠤࡋࡘ࡙ࡖࡓࠣអ") in proxy or bstack11ll1ll_opy_ (u"ࠥࡗࡔࡉࡋࡔࠤឣ") in proxy:
            bstack11l1ll11111_opy_ = proxy.split(bstack11ll1ll_opy_ (u"ࠦࠥࠨឤ"))
            if bstack11ll1ll_opy_ (u"ࠧࡀ࠯࠰ࠤឥ") in bstack11ll1ll_opy_ (u"ࠨࠢឦ").join(bstack11l1ll11111_opy_[1:]):
                proxies = {
                    bstack11ll1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ឧ"): bstack11ll1ll_opy_ (u"ࠣࠤឨ").join(bstack11l1ll11111_opy_[1:])
                }
            else:
                proxies = {
                    bstack11ll1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨឩ"): str(bstack11l1ll11111_opy_[0]).lower() + bstack11ll1ll_opy_ (u"ࠥ࠾࠴࠵ࠢឪ") + bstack11ll1ll_opy_ (u"ࠦࠧឫ").join(bstack11l1ll11111_opy_[1:])
                }
        elif bstack11ll1ll_opy_ (u"ࠧࡖࡒࡐ࡚࡜ࠦឬ") in proxy:
            bstack11l1ll11111_opy_ = proxy.split(bstack11ll1ll_opy_ (u"ࠨࠠࠣឭ"))
            if bstack11ll1ll_opy_ (u"ࠢ࠻࠱࠲ࠦឮ") in bstack11ll1ll_opy_ (u"ࠣࠤឯ").join(bstack11l1ll11111_opy_[1:]):
                proxies = {
                    bstack11ll1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨឰ"): bstack11ll1ll_opy_ (u"ࠥࠦឱ").join(bstack11l1ll11111_opy_[1:])
                }
            else:
                proxies = {
                    bstack11ll1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪឲ"): bstack11ll1ll_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨឳ") + bstack11ll1ll_opy_ (u"ࠨࠢ឴").join(bstack11l1ll11111_opy_[1:])
                }
        else:
            proxies = {
                bstack11ll1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭឵"): proxy
            }
    except Exception as e:
        print(bstack11ll1ll_opy_ (u"ࠣࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠧា"), bstack11l1ll1111l_opy_.format(bstack11l1ll111l1_opy_, str(e)))
    bstack11l1l1llll1_opy_ = proxies
    return proxies