# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1ll1ll1l_opy_
bstack11111111_opy_ = Config.bstack1llll1ll1_opy_()
def bstack11l1ll1llll_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l1ll1lll1_opy_(bstack11l1ll1l111_opy_, bstack11l1ll1l1l1_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l1ll1l111_opy_):
        with open(bstack11l1ll1l111_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l1ll1llll_opy_(bstack11l1ll1l111_opy_):
        pac = get_pac(url=bstack11l1ll1l111_opy_)
    else:
        raise Exception(bstack11l11l1_opy_ (u"࠭ࡐࡢࡥࠣࡪ࡮ࡲࡥࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠼ࠣࡿࢂ࠭ᝧ").format(bstack11l1ll1l111_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack11l11l1_opy_ (u"ࠢ࠹࠰࠻࠲࠽࠴࠸ࠣᝨ"), 80))
        bstack11l1ll1l11l_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l1ll1l11l_opy_ = bstack11l11l1_opy_ (u"ࠨ࠲࠱࠴࠳࠶࠮࠱ࠩᝩ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l1ll1l1l1_opy_, bstack11l1ll1l11l_opy_)
    return proxy_url
def bstack1lll1l1l11_opy_(config):
    return bstack11l11l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬᝪ") in config or bstack11l11l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧᝫ") in config
def bstack1lllll11l1_opy_(config):
    if not bstack1lll1l1l11_opy_(config):
        return
    if config.get(bstack11l11l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᝬ")):
        return config.get(bstack11l11l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ᝭"))
    if config.get(bstack11l11l1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪᝮ")):
        return config.get(bstack11l11l1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫᝯ"))
def bstack11l1ll111_opy_(config, bstack11l1ll1l1l1_opy_):
    proxy = bstack1lllll11l1_opy_(config)
    proxies = {}
    if config.get(bstack11l11l1_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᝰ")) or config.get(bstack11l11l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭᝱")):
        if proxy.endswith(bstack11l11l1_opy_ (u"ࠪ࠲ࡵࡧࡣࠨᝲ")):
            proxies = bstack1111l11lll_opy_(proxy, bstack11l1ll1l1l1_opy_)
        else:
            proxies = {
                bstack11l11l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪᝳ"): proxy
            }
    bstack11111111_opy_.set_property(bstack11l11l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡗࡪࡺࡴࡪࡰࡪࡷࠬ᝴"), proxies)
    return proxies
def bstack1111l11lll_opy_(bstack11l1ll1l111_opy_, bstack11l1ll1l1l1_opy_):
    proxies = {}
    global bstack11l1ll1ll11_opy_
    if bstack11l11l1_opy_ (u"࠭ࡐࡂࡅࡢࡔࡗࡕࡘ࡚ࠩ᝵") in globals():
        return bstack11l1ll1ll11_opy_
    try:
        proxy = bstack11l1ll1lll1_opy_(bstack11l1ll1l111_opy_, bstack11l1ll1l1l1_opy_)
        if bstack11l11l1_opy_ (u"ࠢࡅࡋࡕࡉࡈ࡚ࠢ᝶") in proxy:
            proxies = {}
        elif bstack11l11l1_opy_ (u"ࠣࡊࡗࡘࡕࠨ᝷") in proxy or bstack11l11l1_opy_ (u"ࠤࡋࡘ࡙ࡖࡓࠣ᝸") in proxy or bstack11l11l1_opy_ (u"ࠥࡗࡔࡉࡋࡔࠤ᝹") in proxy:
            bstack11l1ll1l1ll_opy_ = proxy.split(bstack11l11l1_opy_ (u"ࠦࠥࠨ᝺"))
            if bstack11l11l1_opy_ (u"ࠧࡀ࠯࠰ࠤ᝻") in bstack11l11l1_opy_ (u"ࠨࠢ᝼").join(bstack11l1ll1l1ll_opy_[1:]):
                proxies = {
                    bstack11l11l1_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭᝽"): bstack11l11l1_opy_ (u"ࠣࠤ᝾").join(bstack11l1ll1l1ll_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l11l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨ᝿"): str(bstack11l1ll1l1ll_opy_[0]).lower() + bstack11l11l1_opy_ (u"ࠥ࠾࠴࠵ࠢក") + bstack11l11l1_opy_ (u"ࠦࠧខ").join(bstack11l1ll1l1ll_opy_[1:])
                }
        elif bstack11l11l1_opy_ (u"ࠧࡖࡒࡐ࡚࡜ࠦគ") in proxy:
            bstack11l1ll1l1ll_opy_ = proxy.split(bstack11l11l1_opy_ (u"ࠨࠠࠣឃ"))
            if bstack11l11l1_opy_ (u"ࠢ࠻࠱࠲ࠦង") in bstack11l11l1_opy_ (u"ࠣࠤច").join(bstack11l1ll1l1ll_opy_[1:]):
                proxies = {
                    bstack11l11l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨឆ"): bstack11l11l1_opy_ (u"ࠥࠦជ").join(bstack11l1ll1l1ll_opy_[1:])
                }
            else:
                proxies = {
                    bstack11l11l1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࠪឈ"): bstack11l11l1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨញ") + bstack11l11l1_opy_ (u"ࠨࠢដ").join(bstack11l1ll1l1ll_opy_[1:])
                }
        else:
            proxies = {
                bstack11l11l1_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ឋ"): proxy
            }
    except Exception as e:
        print(bstack11l11l1_opy_ (u"ࠣࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠧឌ"), bstack11l1ll1ll1l_opy_.format(bstack11l1ll1l111_opy_, str(e)))
    bstack11l1ll1ll11_opy_ = proxies
    return proxies