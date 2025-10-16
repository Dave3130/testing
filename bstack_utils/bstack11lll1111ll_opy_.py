# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11lll11l1ll_opy_
logger = logging.getLogger(__name__)
class bstack11ll1llllll_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack11ll11llll1_opy_ = urljoin(builder, bstack1ll11_opy_ (u"࠭ࡩࡴࡵࡸࡩࡸ࠭ᚪ"))
        if params:
            bstack11ll11llll1_opy_ += bstack1ll11_opy_ (u"ࠢࡀࡽࢀࠦᚫ").format(urlencode({bstack1ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᚬ"): params.get(bstack1ll11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᚭ"))}))
        return bstack11ll1llllll_opy_.bstack11ll11ll111_opy_(bstack11ll11llll1_opy_)
    @staticmethod
    def bstack11ll1l11l11_opy_(builder,params=None):
        bstack11ll11llll1_opy_ = urljoin(builder, bstack1ll11_opy_ (u"ࠪ࡭ࡸࡹࡵࡦࡵ࠰ࡷࡺࡳ࡭ࡢࡴࡼࠫᚮ"))
        if params:
            bstack11ll11llll1_opy_ += bstack1ll11_opy_ (u"ࠦࡄࢁࡽࠣᚯ").format(urlencode({bstack1ll11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᚰ"): params.get(bstack1ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᚱ"))}))
        return bstack11ll1llllll_opy_.bstack11ll11ll111_opy_(bstack11ll11llll1_opy_)
    @staticmethod
    def bstack11ll11ll111_opy_(bstack11ll11lllll_opy_):
        bstack11ll11lll1l_opy_ = os.environ.get(bstack1ll11_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬᚲ"), os.environ.get(bstack1ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᚳ"), bstack1ll11_opy_ (u"ࠩࠪᚴ")))
        headers = {bstack1ll11_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪᚵ"): bstack1ll11_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧᚶ").format(bstack11ll11lll1l_opy_)}
        response = requests.get(bstack11ll11lllll_opy_, headers=headers)
        bstack11ll11l1ll1_opy_ = {}
        try:
            bstack11ll11l1ll1_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1ll11_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦᚷ").format(e))
            pass
        if bstack11ll11l1ll1_opy_ is not None:
            bstack11ll11l1ll1_opy_[bstack1ll11_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧᚸ")] = response.headers.get(bstack1ll11_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᚹ"), str(int(datetime.now().timestamp() * 1000)))
            bstack11ll11l1ll1_opy_[bstack1ll11_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᚺ")] = response.status_code
        return bstack11ll11l1ll1_opy_
    @staticmethod
    def bstack11lll111l11_opy_(bstack11ll11l1l11_opy_, data):
        logger.debug(bstack1ll11_opy_ (u"ࠤࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡒࡦࡳࡸࡩࡸࡺࠠࡧࡱࡵࠤࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡔࡲ࡯࡭ࡹ࡚ࡥࡴࡶࡶࠦᚻ"))
        return bstack11ll1llllll_opy_.bstack11ll11l1lll_opy_(bstack1ll11_opy_ (u"ࠪࡔࡔ࡙ࡔࠨᚼ"), bstack11ll11l1l11_opy_, data=data)
    @staticmethod
    def bstack11ll1lll111_opy_(bstack11ll11l1l11_opy_, data):
        logger.debug(bstack1ll11_opy_ (u"ࠦࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡔࡨࡵࡺ࡫ࡳࡵࠢࡩࡳࡷࠦࡧࡦࡶࡗࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡲࡥࡧࡵࡩࡩ࡚ࡥࡴࡶࡶࠦᚽ"))
        res = bstack11ll1llllll_opy_.bstack11ll11l1lll_opy_(bstack1ll11_opy_ (u"ࠬࡍࡅࡕࠩᚾ"), bstack11ll11l1l11_opy_, data=data)
        return res
    @staticmethod
    def bstack11ll11l1lll_opy_(method, bstack11ll11l1l11_opy_, data=None, params=None, extra_headers=None):
        bstack11ll11lll1l_opy_ = os.environ.get(bstack1ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᚿ"), bstack1ll11_opy_ (u"ࠧࠨᛀ"))
        headers = {
            bstack1ll11_opy_ (u"ࠨࡣࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨᛁ"): bstack1ll11_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬᛂ").format(bstack11ll11lll1l_opy_),
            bstack1ll11_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩᛃ"): bstack1ll11_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧᛄ"),
            bstack1ll11_opy_ (u"ࠬࡇࡣࡤࡧࡳࡸࠬᛅ"): bstack1ll11_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩᛆ")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11lll11l1ll_opy_ + bstack1ll11_opy_ (u"ࠢ࠰ࠤᛇ") + bstack11ll11l1l11_opy_.lstrip(bstack1ll11_opy_ (u"ࠨ࠱ࠪᛈ"))
        try:
            if method == bstack1ll11_opy_ (u"ࠩࡊࡉ࡙࠭ᛉ"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack1ll11_opy_ (u"ࠪࡔࡔ࡙ࡔࠨᛊ"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack1ll11_opy_ (u"ࠫࡕ࡛ࡔࠨᛋ"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack1ll11_opy_ (u"࡛ࠧ࡮ࡴࡷࡳࡴࡴࡸࡴࡦࡦࠣࡌ࡙࡚ࡐࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠢࡾࢁࠧᛌ").format(method))
            logger.debug(bstack1ll11_opy_ (u"ࠨࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡲࡦࡳࡸࡩࡸࡺࠠ࡮ࡣࡧࡩࠥࡺ࡯ࠡࡗࡕࡐ࠿ࠦࡻࡾࠢࡺ࡭ࡹ࡮ࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠡࡽࢀࠦᛍ").format(url, method))
            bstack11ll11l1ll1_opy_ = {}
            try:
                bstack11ll11l1ll1_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack1ll11_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡸࡳࡦࠢࡍࡗࡔࡔࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠦ࠭ࠡࡽࢀࠦᛎ").format(e, response.text))
            if bstack11ll11l1ll1_opy_ is not None:
                bstack11ll11l1ll1_opy_[bstack1ll11_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᛏ")] = response.headers.get(
                    bstack1ll11_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᛐ"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack11ll11l1ll1_opy_[bstack1ll11_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᛑ")] = response.status_code
            return bstack11ll11l1ll1_opy_
        except Exception as e:
            logger.error(bstack1ll11_opy_ (u"ࠦࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡷ࡫ࡱࡶࡧࡶࡸࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࡻࡾࠢ࠰ࠤࢀࢃࠢᛒ").format(e, url))
            return None
    @staticmethod
    def bstack11ll11l1l1l_opy_(bstack11ll11lllll_opy_, data):
        bstack1ll11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡖࡩࡳࡪࡳࠡࡣࠣࡔ࡚࡚ࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡸ࡭࡫ࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᛓ")
        bstack11ll11lll1l_opy_ = os.environ.get(bstack1ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᛔ"), bstack1ll11_opy_ (u"ࠧࠨᛕ"))
        headers = {
            bstack1ll11_opy_ (u"ࠨࡣࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨᛖ"): bstack1ll11_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬᛗ").format(bstack11ll11lll1l_opy_),
            bstack1ll11_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩᛘ"): bstack1ll11_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧᛙ")
        }
        response = requests.put(bstack11ll11lllll_opy_, headers=headers, json=data)
        bstack11ll11l1ll1_opy_ = {}
        try:
            bstack11ll11l1ll1_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1ll11_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦᛚ").format(e))
            pass
        logger.debug(bstack1ll11_opy_ (u"ࠨࡒࡦࡳࡸࡩࡸࡺࡕࡵ࡫࡯ࡷ࠿ࠦࡰࡶࡶࡢࡪࡦ࡯࡬ࡦࡦࡢࡸࡪࡹࡴࡴࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠣᛛ").format(bstack11ll11l1ll1_opy_))
        if bstack11ll11l1ll1_opy_ is not None:
            bstack11ll11l1ll1_opy_[bstack1ll11_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᛜ")] = response.headers.get(
                bstack1ll11_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᛝ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11l1ll1_opy_[bstack1ll11_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᛞ")] = response.status_code
        return bstack11ll11l1ll1_opy_
    @staticmethod
    def bstack11ll11ll1l1_opy_(bstack11ll11lllll_opy_):
        bstack1ll11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡔࡧࡱࡨࡸࠦࡡࠡࡉࡈࡘࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡪࡩࡹࠦࡴࡩࡧࠣࡧࡴࡻ࡮ࡵࠢࡲࡪࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᛟ")
        bstack11ll11lll1l_opy_ = os.environ.get(bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᛠ"), bstack1ll11_opy_ (u"ࠬ࠭ᛡ"))
        headers = {
            bstack1ll11_opy_ (u"࠭ࡡࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ᛢ"): bstack1ll11_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪᛣ").format(bstack11ll11lll1l_opy_),
            bstack1ll11_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧᛤ"): bstack1ll11_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬᛥ")
        }
        response = requests.get(bstack11ll11lllll_opy_, headers=headers)
        bstack11ll11l1ll1_opy_ = {}
        try:
            bstack11ll11l1ll1_opy_ = response.json()
            logger.debug(bstack1ll11_opy_ (u"ࠥࡖࡪࡷࡵࡦࡵࡷ࡙ࡹ࡯࡬ࡴ࠼ࠣ࡫ࡪࡺ࡟ࡧࡣ࡬ࡰࡪࡪ࡟ࡵࡧࡶࡸࡸࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧᛦ").format(bstack11ll11l1ll1_opy_))
        except Exception as e:
            logger.debug(bstack1ll11_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡊࡔࡑࡑࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠣ࠱ࠥࢁࡽࠣᛧ").format(e, response.text))
            pass
        if bstack11ll11l1ll1_opy_ is not None:
            bstack11ll11l1ll1_opy_[bstack1ll11_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭ᛨ")] = response.headers.get(
                bstack1ll11_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧᛩ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11l1ll1_opy_[bstack1ll11_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᛪ")] = response.status_code
        return bstack11ll11l1ll1_opy_
    @staticmethod
    def bstack11ll11ll1ll_opy_(bstack11ll11lll11_opy_, payload):
        bstack1ll11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡓࡡ࡬ࡧࡶࠤࡦࠦࡐࡐࡕࡗࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡺ࡯ࠡࡶ࡫ࡩࠥࡩ࡯࡭࡮ࡨࡧࡹ࠳ࡢࡶ࡫࡯ࡨ࠲ࡪࡡࡵࡣࠣࡩࡳࡪࡰࡰ࡫ࡱࡸ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡪࡴࡤࡱࡱ࡬ࡲࡹࠦࠨࡴࡶࡵ࠭࠿ࠦࡔࡩࡧࠣࡅࡕࡏࠠࡦࡰࡧࡴࡴ࡯࡮ࡵࠢࡳࡥࡹ࡮࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡰࡢࡻ࡯ࡳࡦࡪࠠࠩࡦ࡬ࡧࡹ࠯࠺ࠡࡖ࡫ࡩࠥࡸࡥࡲࡷࡨࡷࡹࠦࡰࡢࡻ࡯ࡳࡦࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡧ࡭ࡨࡺ࠺ࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡇࡐࡊ࠮ࠣࡳࡷࠦࡎࡰࡰࡨࠤ࡮࡬ࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧ᛫")
        try:
            url = bstack1ll11_opy_ (u"ࠤࡾࢁ࠴ࢁࡽࠣ᛬").format(bstack11lll11l1ll_opy_, bstack11ll11lll11_opy_)
            bstack11ll11lll1l_opy_ = os.environ.get(bstack1ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ᛭"), bstack1ll11_opy_ (u"ࠫࠬᛮ"))
            headers = {
                bstack1ll11_opy_ (u"ࠬࡧࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲࠬᛯ"): bstack1ll11_opy_ (u"࠭ࡂࡦࡣࡵࡩࡷࠦࡻࡾࠩᛰ").format(bstack11ll11lll1l_opy_),
                bstack1ll11_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭ᛱ"): bstack1ll11_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫᛲ")
            }
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            bstack11ll11ll11l_opy_ = [200, 202]
            if response.status_code in bstack11ll11ll11l_opy_:
                return response.json()
            else:
                logger.error(bstack1ll11_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡩ࡯࡭࡮ࡨࡧࡹࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣ࠱ࠤࡘࡺࡡࡵࡷࡶ࠾ࠥࢁࡽ࠭ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠣᛳ").format(
                    response.status_code, response.text))
                return None
        except Exception as e:
            logger.error(bstack1ll11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡳࡸࡺ࡟ࡤࡱ࡯ࡰࡪࡩࡴࡠࡤࡸ࡭ࡱࡪ࡟ࡥࡣࡷࡥ࠿ࠦࡻࡾࠤᛴ").format(e))
            return None