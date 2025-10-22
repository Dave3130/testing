# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack11l1ll11lll_opy_
bstack1lllll1l1_opy_ = Config.bstack1111ll1l_opy_()
def bstack11l1ll11ll1_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11l1ll11l11_opy_(bstack11l1ll1l11l_opy_, bstack11l1ll1l111_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11l1ll1l11l_opy_):
        with open(bstack11l1ll1l11l_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11l1ll11ll1_opy_(bstack11l1ll1l11l_opy_):
        pac = get_pac(url=bstack11l1ll1l11l_opy_)
    else:
        raise Exception(bstack111l1l_opy_ (u"ࠧࡑࡣࡦࠤ࡫࡯࡬ࡦࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡪࡾࡩࡴࡶ࠽ࠤࢀࢃࠧᝯ").format(bstack11l1ll1l11l_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack111l1l_opy_ (u"ࠣ࠺࠱࠼࠳࠾࠮࠹ࠤᝰ"), 80))
        bstack11l1ll11l1l_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11l1ll11l1l_opy_ = bstack111l1l_opy_ (u"ࠩ࠳࠲࠵࠴࠰࠯࠲ࠪ᝱")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11l1ll1l111_opy_, bstack11l1ll11l1l_opy_)
    return proxy_url
def bstack111ll1lll1_opy_(config):
    return bstack111l1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ᝲ") in config or bstack111l1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨᝳ") in config
def bstack111ll11ll_opy_(config):
    if not bstack111ll1lll1_opy_(config):
        return
    if config.get(bstack111l1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ᝴")):
        return config.get(bstack111l1l_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ᝵"))
    if config.get(bstack111l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ᝶")):
        return config.get(bstack111l1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ᝷"))
def bstack1l1111l1l1_opy_(config, bstack11l1ll1l111_opy_):
    proxy = bstack111ll11ll_opy_(config)
    proxies = {}
    if config.get(bstack111l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ᝸")) or config.get(bstack111l1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧ᝹")):
        if proxy.endswith(bstack111l1l_opy_ (u"ࠫ࠳ࡶࡡࡤࠩ᝺")):
            proxies = bstack1l11l1ll1_opy_(proxy, bstack11l1ll1l111_opy_)
        else:
            proxies = {
                bstack111l1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫ᝻"): proxy
            }
    bstack1lllll1l1_opy_.set_property(bstack111l1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡘ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭᝼"), proxies)
    return proxies
def bstack1l11l1ll1_opy_(bstack11l1ll1l11l_opy_, bstack11l1ll1l111_opy_):
    proxies = {}
    global bstack11l1ll1l1l1_opy_
    if bstack111l1l_opy_ (u"ࠧࡑࡃࡆࡣࡕࡘࡏ࡙࡛ࠪ᝽") in globals():
        return bstack11l1ll1l1l1_opy_
    try:
        proxy = bstack11l1ll11l11_opy_(bstack11l1ll1l11l_opy_, bstack11l1ll1l111_opy_)
        if bstack111l1l_opy_ (u"ࠣࡆࡌࡖࡊࡉࡔࠣ᝾") in proxy:
            proxies = {}
        elif bstack111l1l_opy_ (u"ࠤࡋࡘ࡙ࡖࠢ᝿") in proxy or bstack111l1l_opy_ (u"ࠥࡌ࡙࡚ࡐࡔࠤក") in proxy or bstack111l1l_opy_ (u"ࠦࡘࡕࡃࡌࡕࠥខ") in proxy:
            bstack11l1ll1l1ll_opy_ = proxy.split(bstack111l1l_opy_ (u"ࠧࠦࠢគ"))
            if bstack111l1l_opy_ (u"ࠨ࠺࠰࠱ࠥឃ") in bstack111l1l_opy_ (u"ࠢࠣង").join(bstack11l1ll1l1ll_opy_[1:]):
                proxies = {
                    bstack111l1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧច"): bstack111l1l_opy_ (u"ࠤࠥឆ").join(bstack11l1ll1l1ll_opy_[1:])
                }
            else:
                proxies = {
                    bstack111l1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩជ"): str(bstack11l1ll1l1ll_opy_[0]).lower() + bstack111l1l_opy_ (u"ࠦ࠿࠵࠯ࠣឈ") + bstack111l1l_opy_ (u"ࠧࠨញ").join(bstack11l1ll1l1ll_opy_[1:])
                }
        elif bstack111l1l_opy_ (u"ࠨࡐࡓࡑ࡛࡝ࠧដ") in proxy:
            bstack11l1ll1l1ll_opy_ = proxy.split(bstack111l1l_opy_ (u"ࠢࠡࠤឋ"))
            if bstack111l1l_opy_ (u"ࠣ࠼࠲࠳ࠧឌ") in bstack111l1l_opy_ (u"ࠤࠥឍ").join(bstack11l1ll1l1ll_opy_[1:]):
                proxies = {
                    bstack111l1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩណ"): bstack111l1l_opy_ (u"ࠦࠧត").join(bstack11l1ll1l1ll_opy_[1:])
                }
            else:
                proxies = {
                    bstack111l1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫថ"): bstack111l1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢទ") + bstack111l1l_opy_ (u"ࠢࠣធ").join(bstack11l1ll1l1ll_opy_[1:])
                }
        else:
            proxies = {
                bstack111l1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࠧន"): proxy
            }
    except Exception as e:
        print(bstack111l1l_opy_ (u"ࠤࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷࠨប"), bstack11l1ll11lll_opy_.format(bstack11l1ll1l11l_opy_, str(e)))
    bstack11l1ll1l1l1_opy_ = proxies
    return proxies