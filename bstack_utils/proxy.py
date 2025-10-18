# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1ll1l1ll_opy_
bstack1111l111_opy_ = Config.bstack11111ll1_opy_()
def bstack11l1ll1l1l1_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l1ll1l111_opy_(bstack11l1ll11ll1_opy_, bstack11l1ll11lll_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l1ll11ll1_opy_):
        with open(bstack11l1ll11ll1_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l1ll1l1l1_opy_(bstack11l1ll11ll1_opy_):
        pac = get_pac(url=bstack11l1ll11ll1_opy_)
    else:
        raise Exception(bstack11ll_opy_ (u"ࠧࡑࡣࡦࠤ࡫࡯࡬ࡦࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡪࡾࡩࡴࡶ࠽ࠤࢀࢃࠧ᝶").format(bstack11l1ll11ll1_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack11ll_opy_ (u"ࠣ࠺࠱࠼࠳࠾࠮࠹ࠤ᝷"), 80))
        bstack11l1ll11l1l_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l1ll11l1l_opy_ = bstack11ll_opy_ (u"ࠩ࠳࠲࠵࠴࠰࠯࠲ࠪ᝸")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l1ll11lll_opy_, bstack11l1ll11l1l_opy_)
    return proxy_url
def bstack11l1l1l1l1_opy_(config):
    return bstack11ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭᝹") in config or bstack11ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨ᝺") in config
def bstack111lll1l1l_opy_(config):
    if not bstack11l1l1l1l1_opy_(config):
        return
    if config.get(bstack11ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ᝻")):
        return config.get(bstack11ll_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ᝼"))
    if config.get(bstack11ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ᝽")):
        return config.get(bstack11ll_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ᝾"))
def bstack1l1lll1l1l_opy_(config, bstack11l1ll11lll_opy_):
    proxy = bstack111lll1l1l_opy_(config)
    proxies = {}
    if config.get(bstack11ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ᝿")) or config.get(bstack11ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧក")):
        if proxy.endswith(bstack11ll_opy_ (u"ࠫ࠳ࡶࡡࡤࠩខ")):
            proxies = bstack111ll1l1ll_opy_(proxy, bstack11l1ll11lll_opy_)
        else:
            proxies = {
                bstack11ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫគ"): proxy
            }
    bstack1111l111_opy_.set_property(bstack11ll_opy_ (u"࠭ࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭ឃ"), proxies)
    return proxies
def bstack111ll1l1ll_opy_(bstack11l1ll11ll1_opy_, bstack11l1ll11lll_opy_):
    proxies = {}
    global bstack11l1ll1ll11_opy_
    if bstack11ll_opy_ (u"ࠧࡑࡃࡆࡣࡕࡘࡏ࡙࡛ࠪង") in globals():
        return bstack11l1ll1ll11_opy_
    try:
        proxy = bstack11l1ll1l111_opy_(bstack11l1ll11ll1_opy_, bstack11l1ll11lll_opy_)
        if bstack11ll_opy_ (u"ࠣࡆࡌࡖࡊࡉࡔࠣច") in proxy:
            proxies = {}
        elif bstack11ll_opy_ (u"ࠤࡋࡘ࡙ࡖࠢឆ") in proxy or bstack11ll_opy_ (u"ࠥࡌ࡙࡚ࡐࡔࠤជ") in proxy or bstack11ll_opy_ (u"ࠦࡘࡕࡃࡌࡕࠥឈ") in proxy:
            bstack11l1ll1l11l_opy_ = proxy.split(bstack11ll_opy_ (u"ࠧࠦࠢញ"))
            if bstack11ll_opy_ (u"ࠨ࠺࠰࠱ࠥដ") in bstack11ll_opy_ (u"ࠢࠣឋ").join(bstack11l1ll1l11l_opy_[1:]):
                proxies = {
                    bstack11ll_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧឌ"): bstack11ll_opy_ (u"ࠤࠥឍ").join(bstack11l1ll1l11l_opy_[1:])
                }
            else:
                proxies = {
                    bstack11ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩណ"): str(bstack11l1ll1l11l_opy_[0]).lower() + bstack11ll_opy_ (u"ࠦ࠿࠵࠯ࠣត") + bstack11ll_opy_ (u"ࠧࠨថ").join(bstack11l1ll1l11l_opy_[1:])
                }
        elif bstack11ll_opy_ (u"ࠨࡐࡓࡑ࡛࡝ࠧទ") in proxy:
            bstack11l1ll1l11l_opy_ = proxy.split(bstack11ll_opy_ (u"ࠢࠡࠤធ"))
            if bstack11ll_opy_ (u"ࠣ࠼࠲࠳ࠧន") in bstack11ll_opy_ (u"ࠤࠥប").join(bstack11l1ll1l11l_opy_[1:]):
                proxies = {
                    bstack11ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩផ"): bstack11ll_opy_ (u"ࠦࠧព").join(bstack11l1ll1l11l_opy_[1:])
                }
            else:
                proxies = {
                    bstack11ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫភ"): bstack11ll_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢម") + bstack11ll_opy_ (u"ࠢࠣយ").join(bstack11l1ll1l11l_opy_[1:])
                }
        else:
            proxies = {
                bstack11ll_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧរ"): proxy
            }
    except Exception as e:
        print(bstack11ll_opy_ (u"ࠤࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷࠨល"), bstack11l1ll1l1ll_opy_.format(bstack11l1ll11ll1_opy_, str(e)))
    bstack11l1ll1ll11_opy_ = proxies
    return proxies