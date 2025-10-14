# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11ll1llllll_opy_
logger = logging.getLogger(__name__)
class bstack11ll1lllll1_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack11ll11lll1l_opy_ = urljoin(builder, bstack11l1l11_opy_ (u"࠭ࡩࡴࡵࡸࡩࡸ࠭ᚣ"))
        if params:
            bstack11ll11lll1l_opy_ += bstack11l1l11_opy_ (u"ࠢࡀࡽࢀࠦᚤ").format(urlencode({bstack11l1l11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᚥ"): params.get(bstack11l1l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᚦ"))}))
        return bstack11ll1lllll1_opy_.bstack11ll11ll1ll_opy_(bstack11ll11lll1l_opy_)
    @staticmethod
    def bstack11ll1l1111l_opy_(builder,params=None):
        bstack11ll11lll1l_opy_ = urljoin(builder, bstack11l1l11_opy_ (u"ࠪ࡭ࡸࡹࡵࡦࡵ࠰ࡷࡺࡳ࡭ࡢࡴࡼࠫᚧ"))
        if params:
            bstack11ll11lll1l_opy_ += bstack11l1l11_opy_ (u"ࠦࡄࢁࡽࠣᚨ").format(urlencode({bstack11l1l11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᚩ"): params.get(bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᚪ"))}))
        return bstack11ll1lllll1_opy_.bstack11ll11ll1ll_opy_(bstack11ll11lll1l_opy_)
    @staticmethod
    def bstack11ll11ll1ll_opy_(bstack11ll11l1lll_opy_):
        bstack11ll11ll1l1_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬᚫ"), os.environ.get(bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᚬ"), bstack11l1l11_opy_ (u"ࠩࠪᚭ")))
        headers = {bstack11l1l11_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪᚮ"): bstack11l1l11_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧᚯ").format(bstack11ll11ll1l1_opy_)}
        response = requests.get(bstack11ll11l1lll_opy_, headers=headers)
        bstack11ll11ll111_opy_ = {}
        try:
            bstack11ll11ll111_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦᚰ").format(e))
            pass
        if bstack11ll11ll111_opy_ is not None:
            bstack11ll11ll111_opy_[bstack11l1l11_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧᚱ")] = response.headers.get(bstack11l1l11_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᚲ"), str(int(datetime.now().timestamp() * 1000)))
            bstack11ll11ll111_opy_[bstack11l1l11_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᚳ")] = response.status_code
        return bstack11ll11ll111_opy_
    @staticmethod
    def bstack11ll1ll1l11_opy_(bstack11ll11l1l1l_opy_, data):
        logger.debug(bstack11l1l11_opy_ (u"ࠤࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡒࡦࡳࡸࡩࡸࡺࠠࡧࡱࡵࠤࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡔࡲ࡯࡭ࡹ࡚ࡥࡴࡶࡶࠦᚴ"))
        return bstack11ll1lllll1_opy_.bstack11ll11ll11l_opy_(bstack11l1l11_opy_ (u"ࠪࡔࡔ࡙ࡔࠨᚵ"), bstack11ll11l1l1l_opy_, data=data)
    @staticmethod
    def bstack11lll11l1ll_opy_(bstack11ll11l1l1l_opy_, data):
        logger.debug(bstack11l1l11_opy_ (u"ࠦࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡔࡨࡵࡺ࡫ࡳࡵࠢࡩࡳࡷࠦࡧࡦࡶࡗࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡲࡥࡧࡵࡩࡩ࡚ࡥࡴࡶࡶࠦᚶ"))
        res = bstack11ll1lllll1_opy_.bstack11ll11ll11l_opy_(bstack11l1l11_opy_ (u"ࠬࡍࡅࡕࠩᚷ"), bstack11ll11l1l1l_opy_, data=data)
        return res
    @staticmethod
    def bstack11ll11ll11l_opy_(method, bstack11ll11l1l1l_opy_, data=None, params=None, extra_headers=None):
        bstack11ll11ll1l1_opy_ = os.environ.get(bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᚸ"), bstack11l1l11_opy_ (u"ࠧࠨᚹ"))
        headers = {
            bstack11l1l11_opy_ (u"ࠨࡣࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨᚺ"): bstack11l1l11_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬᚻ").format(bstack11ll11ll1l1_opy_),
            bstack11l1l11_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩᚼ"): bstack11l1l11_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧᚽ"),
            bstack11l1l11_opy_ (u"ࠬࡇࡣࡤࡧࡳࡸࠬᚾ"): bstack11l1l11_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩᚿ")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11ll1llllll_opy_ + bstack11l1l11_opy_ (u"ࠢ࠰ࠤᛀ") + bstack11ll11l1l1l_opy_.lstrip(bstack11l1l11_opy_ (u"ࠨ࠱ࠪᛁ"))
        try:
            if method == bstack11l1l11_opy_ (u"ࠩࡊࡉ࡙࠭ᛂ"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack11l1l11_opy_ (u"ࠪࡔࡔ࡙ࡔࠨᛃ"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack11l1l11_opy_ (u"ࠫࡕ࡛ࡔࠨᛄ"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack11l1l11_opy_ (u"࡛ࠧ࡮ࡴࡷࡳࡴࡴࡸࡴࡦࡦࠣࡌ࡙࡚ࡐࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠢࡾࢁࠧᛅ").format(method))
            logger.debug(bstack11l1l11_opy_ (u"ࠨࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡲࡦࡳࡸࡩࡸࡺࠠ࡮ࡣࡧࡩࠥࡺ࡯ࠡࡗࡕࡐ࠿ࠦࡻࡾࠢࡺ࡭ࡹ࡮ࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠡࡽࢀࠦᛆ").format(url, method))
            bstack11ll11ll111_opy_ = {}
            try:
                bstack11ll11ll111_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack11l1l11_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡸࡳࡦࠢࡍࡗࡔࡔࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠦ࠭ࠡࡽࢀࠦᛇ").format(e, response.text))
            if bstack11ll11ll111_opy_ is not None:
                bstack11ll11ll111_opy_[bstack11l1l11_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᛈ")] = response.headers.get(
                    bstack11l1l11_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᛉ"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack11ll11ll111_opy_[bstack11l1l11_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᛊ")] = response.status_code
            return bstack11ll11ll111_opy_
        except Exception as e:
            logger.error(bstack11l1l11_opy_ (u"ࠦࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡷ࡫ࡱࡶࡧࡶࡸࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࡻࡾࠢ࠰ࠤࢀࢃࠢᛋ").format(e, url))
            return None
    @staticmethod
    def bstack11ll11l11ll_opy_(bstack11ll11l1lll_opy_, data):
        bstack11l1l11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡖࡩࡳࡪࡳࠡࡣࠣࡔ࡚࡚ࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡸ࡭࡫ࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᛌ")
        bstack11ll11ll1l1_opy_ = os.environ.get(bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᛍ"), bstack11l1l11_opy_ (u"ࠧࠨᛎ"))
        headers = {
            bstack11l1l11_opy_ (u"ࠨࡣࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨᛏ"): bstack11l1l11_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬᛐ").format(bstack11ll11ll1l1_opy_),
            bstack11l1l11_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩᛑ"): bstack11l1l11_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧᛒ")
        }
        response = requests.put(bstack11ll11l1lll_opy_, headers=headers, json=data)
        bstack11ll11ll111_opy_ = {}
        try:
            bstack11ll11ll111_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦᛓ").format(e))
            pass
        logger.debug(bstack11l1l11_opy_ (u"ࠨࡒࡦࡳࡸࡩࡸࡺࡕࡵ࡫࡯ࡷ࠿ࠦࡰࡶࡶࡢࡪࡦ࡯࡬ࡦࡦࡢࡸࡪࡹࡴࡴࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠣᛔ").format(bstack11ll11ll111_opy_))
        if bstack11ll11ll111_opy_ is not None:
            bstack11ll11ll111_opy_[bstack11l1l11_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᛕ")] = response.headers.get(
                bstack11l1l11_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᛖ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11ll111_opy_[bstack11l1l11_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᛗ")] = response.status_code
        return bstack11ll11ll111_opy_
    @staticmethod
    def bstack11ll11lll11_opy_(bstack11ll11l1lll_opy_):
        bstack11l1l11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡔࡧࡱࡨࡸࠦࡡࠡࡉࡈࡘࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡪࡩࡹࠦࡴࡩࡧࠣࡧࡴࡻ࡮ࡵࠢࡲࡪࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᛘ")
        bstack11ll11ll1l1_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᛙ"), bstack11l1l11_opy_ (u"ࠬ࠭ᛚ"))
        headers = {
            bstack11l1l11_opy_ (u"࠭ࡡࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ᛛ"): bstack11l1l11_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪᛜ").format(bstack11ll11ll1l1_opy_),
            bstack11l1l11_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧᛝ"): bstack11l1l11_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬᛞ")
        }
        response = requests.get(bstack11ll11l1lll_opy_, headers=headers)
        bstack11ll11ll111_opy_ = {}
        try:
            bstack11ll11ll111_opy_ = response.json()
            logger.debug(bstack11l1l11_opy_ (u"ࠥࡖࡪࡷࡵࡦࡵࡷ࡙ࡹ࡯࡬ࡴ࠼ࠣ࡫ࡪࡺ࡟ࡧࡣ࡬ࡰࡪࡪ࡟ࡵࡧࡶࡸࡸࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧᛟ").format(bstack11ll11ll111_opy_))
        except Exception as e:
            logger.debug(bstack11l1l11_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡊࡔࡑࡑࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠣ࠱ࠥࢁࡽࠣᛠ").format(e, response.text))
            pass
        if bstack11ll11ll111_opy_ is not None:
            bstack11ll11ll111_opy_[bstack11l1l11_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭ᛡ")] = response.headers.get(
                bstack11l1l11_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧᛢ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11ll111_opy_[bstack11l1l11_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᛣ")] = response.status_code
        return bstack11ll11ll111_opy_
    @staticmethod
    def bstack11ll11l11l1_opy_(bstack11ll11l1ll1_opy_, payload):
        bstack11l1l11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡓࡡ࡬ࡧࡶࠤࡦࠦࡐࡐࡕࡗࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡺ࡯ࠡࡶ࡫ࡩࠥࡩ࡯࡭࡮ࡨࡧࡹ࠳ࡢࡶ࡫࡯ࡨ࠲ࡪࡡࡵࡣࠣࡩࡳࡪࡰࡰ࡫ࡱࡸ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡪࡴࡤࡱࡱ࡬ࡲࡹࠦࠨࡴࡶࡵ࠭࠿ࠦࡔࡩࡧࠣࡅࡕࡏࠠࡦࡰࡧࡴࡴ࡯࡮ࡵࠢࡳࡥࡹ࡮࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡰࡢࡻ࡯ࡳࡦࡪࠠࠩࡦ࡬ࡧࡹ࠯࠺ࠡࡖ࡫ࡩࠥࡸࡥࡲࡷࡨࡷࡹࠦࡰࡢࡻ࡯ࡳࡦࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡧ࡭ࡨࡺ࠺ࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡇࡐࡊ࠮ࠣࡳࡷࠦࡎࡰࡰࡨࠤ࡮࡬ࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᛤ")
        try:
            url = bstack11l1l11_opy_ (u"ࠤࡾࢁ࠴ࢁࡽࠣᛥ").format(bstack11ll1llllll_opy_, bstack11ll11l1ll1_opy_)
            bstack11ll11ll1l1_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧᛦ"), bstack11l1l11_opy_ (u"ࠫࠬᛧ"))
            headers = {
                bstack11l1l11_opy_ (u"ࠬࡧࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲࠬᛨ"): bstack11l1l11_opy_ (u"࠭ࡂࡦࡣࡵࡩࡷࠦࡻࡾࠩᛩ").format(bstack11ll11ll1l1_opy_),
                bstack11l1l11_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭ᛪ"): bstack11l1l11_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫ᛫")
            }
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            bstack11ll11l1l11_opy_ = [200, 202]
            if response.status_code in bstack11ll11l1l11_opy_:
                return response.json()
            else:
                logger.error(bstack11l1l11_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡩ࡯࡭࡮ࡨࡧࡹࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣ࠱ࠤࡘࡺࡡࡵࡷࡶ࠾ࠥࢁࡽ࠭ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠣ᛬").format(
                    response.status_code, response.text))
                return None
        except Exception as e:
            logger.error(bstack11l1l11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡳࡸࡺ࡟ࡤࡱ࡯ࡰࡪࡩࡴࡠࡤࡸ࡭ࡱࡪ࡟ࡥࡣࡷࡥ࠿ࠦࡻࡾࠤ᛭").format(e))
            return None