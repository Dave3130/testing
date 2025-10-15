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
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11ll1ll1lll_opy_
logger = logging.getLogger(__name__)
class bstack11ll1ll1ll1_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack11ll11l11l1_opy_ = urljoin(builder, bstack1ll1l_opy_ (u"ࠨ࡫ࡶࡷࡺ࡫ࡳࠨᚥ"))
        if params:
            bstack11ll11l11l1_opy_ += bstack1ll1l_opy_ (u"ࠤࡂࡿࢂࠨᚦ").format(urlencode({bstack1ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᚧ"): params.get(bstack1ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᚨ"))}))
        return bstack11ll1ll1ll1_opy_.bstack11ll11lll11_opy_(bstack11ll11l11l1_opy_)
    @staticmethod
    def bstack11ll11llll1_opy_(builder,params=None):
        bstack11ll11l11l1_opy_ = urljoin(builder, bstack1ll1l_opy_ (u"ࠬ࡯ࡳࡴࡷࡨࡷ࠲ࡹࡵ࡮࡯ࡤࡶࡾ࠭ᚩ"))
        if params:
            bstack11ll11l11l1_opy_ += bstack1ll1l_opy_ (u"ࠨ࠿ࡼࡿࠥᚪ").format(urlencode({bstack1ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᚫ"): params.get(bstack1ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᚬ"))}))
        return bstack11ll1ll1ll1_opy_.bstack11ll11lll11_opy_(bstack11ll11l11l1_opy_)
    @staticmethod
    def bstack11ll11lll11_opy_(bstack11ll11ll1l1_opy_):
        bstack11ll11ll1ll_opy_ = os.environ.get(bstack1ll1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧᚭ"), os.environ.get(bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧᚮ"), bstack1ll1l_opy_ (u"ࠫࠬᚯ")))
        headers = {bstack1ll1l_opy_ (u"ࠬࡇࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲࠬᚰ"): bstack1ll1l_opy_ (u"࠭ࡂࡦࡣࡵࡩࡷࠦࡻࡾࠩᚱ").format(bstack11ll11ll1ll_opy_)}
        response = requests.get(bstack11ll11ll1l1_opy_, headers=headers)
        bstack11ll11lll1l_opy_ = {}
        try:
            bstack11ll11lll1l_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1ll1l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡸࡳࡦࠢࡍࡗࡔࡔࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨᚲ").format(e))
            pass
        if bstack11ll11lll1l_opy_ is not None:
            bstack11ll11lll1l_opy_[bstack1ll1l_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᚳ")] = response.headers.get(bstack1ll1l_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᚴ"), str(int(datetime.now().timestamp() * 1000)))
            bstack11ll11lll1l_opy_[bstack1ll1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᚵ")] = response.status_code
        return bstack11ll11lll1l_opy_
    @staticmethod
    def bstack11lll11l1ll_opy_(bstack11ll11ll11l_opy_, data):
        logger.debug(bstack1ll1l_opy_ (u"ࠦࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡔࡨࡵࡺ࡫ࡳࡵࠢࡩࡳࡷࠦࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡖࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࠨᚶ"))
        return bstack11ll1ll1ll1_opy_.bstack11ll11l1l11_opy_(bstack1ll1l_opy_ (u"ࠬࡖࡏࡔࡖࠪᚷ"), bstack11ll11ll11l_opy_, data=data)
    @staticmethod
    def bstack11lll111111_opy_(bstack11ll11ll11l_opy_, data):
        logger.debug(bstack1ll1l_opy_ (u"ࠨࡐࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡖࡪࡷࡵࡦࡵࡷࠤ࡫ࡵࡲࠡࡩࡨࡸ࡙࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡸࠨᚸ"))
        res = bstack11ll1ll1ll1_opy_.bstack11ll11l1l11_opy_(bstack1ll1l_opy_ (u"ࠧࡈࡇࡗࠫᚹ"), bstack11ll11ll11l_opy_, data=data)
        return res
    @staticmethod
    def bstack11ll11l1l11_opy_(method, bstack11ll11ll11l_opy_, data=None, params=None, extra_headers=None):
        bstack11ll11ll1ll_opy_ = os.environ.get(bstack1ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᚺ"), bstack1ll1l_opy_ (u"ࠩࠪᚻ"))
        headers = {
            bstack1ll1l_opy_ (u"ࠪࡥࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪᚼ"): bstack1ll1l_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧᚽ").format(bstack11ll11ll1ll_opy_),
            bstack1ll1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫᚾ"): bstack1ll1l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩᚿ"),
            bstack1ll1l_opy_ (u"ࠧࡂࡥࡦࡩࡵࡺࠧᛀ"): bstack1ll1l_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫᛁ")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11ll1ll1lll_opy_ + bstack1ll1l_opy_ (u"ࠤ࠲ࠦᛂ") + bstack11ll11ll11l_opy_.lstrip(bstack1ll1l_opy_ (u"ࠪ࠳ࠬᛃ"))
        try:
            if method == bstack1ll1l_opy_ (u"ࠫࡌࡋࡔࠨᛄ"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack1ll1l_opy_ (u"ࠬࡖࡏࡔࡖࠪᛅ"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack1ll1l_opy_ (u"࠭ࡐࡖࡖࠪᛆ"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack1ll1l_opy_ (u"ࠢࡖࡰࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࠥࡎࡔࡕࡒࠣࡱࡪࡺࡨࡰࡦ࠽ࠤࢀࢃࠢᛇ").format(method))
            logger.debug(bstack1ll1l_opy_ (u"ࠣࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡰࡥࡩ࡫ࠠࡵࡱ࡙ࠣࡗࡒ࠺ࠡࡽࢀࠤࡼ࡯ࡴࡩࠢࡰࡩࡹ࡮࡯ࡥ࠼ࠣࡿࢂࠨᛈ").format(url, method))
            bstack11ll11lll1l_opy_ = {}
            try:
                bstack11ll11lll1l_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack1ll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤࡏ࡙ࡏࡏࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠡ࠯ࠣࡿࢂࠨᛉ").format(e, response.text))
            if bstack11ll11lll1l_opy_ is not None:
                bstack11ll11lll1l_opy_[bstack1ll1l_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᛊ")] = response.headers.get(
                    bstack1ll1l_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬᛋ"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack11ll11lll1l_opy_[bstack1ll1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᛌ")] = response.status_code
            return bstack11ll11lll1l_opy_
        except Exception as e:
            logger.error(bstack1ll1l_opy_ (u"ࠨࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡲࡦࡳࡸࡩࡸࡺࠠࡧࡣ࡬ࡰࡪࡪ࠺ࠡࡽࢀࠤ࠲ࠦࡻࡾࠤᛍ").format(e, url))
            return None
    @staticmethod
    def bstack11ll11l11ll_opy_(bstack11ll11ll1l1_opy_, data):
        bstack1ll1l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡘ࡫࡮ࡥࡵࠣࡥࠥࡖࡕࡕࠢࡵࡩࡶࡻࡥࡴࡶࠣࡸࡴࠦࡳࡵࡱࡵࡩࠥࡺࡨࡦࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡩࡸࡺࡳࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᛎ")
        bstack11ll11ll1ll_opy_ = os.environ.get(bstack1ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᛏ"), bstack1ll1l_opy_ (u"ࠩࠪᛐ"))
        headers = {
            bstack1ll1l_opy_ (u"ࠪࡥࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪᛑ"): bstack1ll1l_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧᛒ").format(bstack11ll11ll1ll_opy_),
            bstack1ll1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫᛓ"): bstack1ll1l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩᛔ")
        }
        response = requests.put(bstack11ll11ll1l1_opy_, headers=headers, json=data)
        bstack11ll11lll1l_opy_ = {}
        try:
            bstack11ll11lll1l_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1ll1l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡸࡳࡦࠢࡍࡗࡔࡔࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨᛕ").format(e))
            pass
        logger.debug(bstack1ll1l_opy_ (u"ࠣࡔࡨࡵࡺ࡫ࡳࡵࡗࡷ࡭ࡱࡹ࠺ࠡࡲࡸࡸࡤ࡬ࡡࡪ࡮ࡨࡨࡤࡺࡥࡴࡶࡶࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥᛖ").format(bstack11ll11lll1l_opy_))
        if bstack11ll11lll1l_opy_ is not None:
            bstack11ll11lll1l_opy_[bstack1ll1l_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᛗ")] = response.headers.get(
                bstack1ll1l_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᛘ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11lll1l_opy_[bstack1ll1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᛙ")] = response.status_code
        return bstack11ll11lll1l_opy_
    @staticmethod
    def bstack11ll11ll111_opy_(bstack11ll11ll1l1_opy_):
        bstack1ll1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡖࡩࡳࡪࡳࠡࡣࠣࡋࡊ࡚ࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤ࡬࡫ࡴࠡࡶ࡫ࡩࠥࡩ࡯ࡶࡰࡷࠤࡴ࡬ࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡧࡶࡸࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᛚ")
        bstack11ll11ll1ll_opy_ = os.environ.get(bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᛛ"), bstack1ll1l_opy_ (u"ࠧࠨᛜ"))
        headers = {
            bstack1ll1l_opy_ (u"ࠨࡣࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨᛝ"): bstack1ll1l_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬᛞ").format(bstack11ll11ll1ll_opy_),
            bstack1ll1l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩᛟ"): bstack1ll1l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧᛠ")
        }
        response = requests.get(bstack11ll11ll1l1_opy_, headers=headers)
        bstack11ll11lll1l_opy_ = {}
        try:
            bstack11ll11lll1l_opy_ = response.json()
            logger.debug(bstack1ll1l_opy_ (u"ࠧࡘࡥࡲࡷࡨࡷࡹ࡛ࡴࡪ࡮ࡶ࠾ࠥ࡭ࡥࡵࡡࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠢᛡ").format(bstack11ll11lll1l_opy_))
        except Exception as e:
            logger.debug(bstack1ll1l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡌࡖࡓࡓࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠥ࠳ࠠࡼࡿࠥᛢ").format(e, response.text))
            pass
        if bstack11ll11lll1l_opy_ is not None:
            bstack11ll11lll1l_opy_[bstack1ll1l_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᛣ")] = response.headers.get(
                bstack1ll1l_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᛤ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11lll1l_opy_[bstack1ll1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᛥ")] = response.status_code
        return bstack11ll11lll1l_opy_
    @staticmethod
    def bstack11ll11l1l1l_opy_(bstack11ll11l1lll_opy_, payload):
        bstack1ll1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡎࡣ࡮ࡩࡸࠦࡡࠡࡒࡒࡗ࡙ࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣࡸ࡭࡫ࠠࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡤࡸ࡭ࡱࡪ࠭ࡥࡣࡷࡥࠥ࡫࡮ࡥࡲࡲ࡭ࡳࡺ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡥ࡯ࡦࡳࡳ࡮ࡴࡴࠡࠪࡶࡸࡷ࠯࠺ࠡࡖ࡫ࡩࠥࡇࡐࡊࠢࡨࡲࡩࡶ࡯ࡪࡰࡷࠤࡵࡧࡴࡩ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡲࡤࡽࡱࡵࡡࡥࠢࠫࡨ࡮ࡩࡴࠪ࠼ࠣࡘ࡭࡫ࠠࡳࡧࡴࡹࡪࡹࡴࠡࡲࡤࡽࡱࡵࡡࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡩ࡯ࡣࡵ࠼ࠣࡖࡪࡹࡰࡰࡰࡶࡩࠥ࡬ࡲࡰ࡯ࠣࡸ࡭࡫ࠠࡂࡒࡌ࠰ࠥࡵࡲࠡࡐࡲࡲࡪࠦࡩࡧࠢࡩࡥ࡮ࡲࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᛦ")
        try:
            url = bstack1ll1l_opy_ (u"ࠦࢀࢃ࠯ࡼࡿࠥᛧ").format(bstack11ll1ll1lll_opy_, bstack11ll11l1lll_opy_)
            bstack11ll11ll1ll_opy_ = os.environ.get(bstack1ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩᛨ"), bstack1ll1l_opy_ (u"࠭ࠧᛩ"))
            headers = {
                bstack1ll1l_opy_ (u"ࠧࡢࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧᛪ"): bstack1ll1l_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࡽࢀࠫ᛫").format(bstack11ll11ll1ll_opy_),
                bstack1ll1l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨ᛬"): bstack1ll1l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭᛭")
            }
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            bstack11ll11l1ll1_opy_ = [200, 202]
            if response.status_code in bstack11ll11l1ll1_opy_:
                return response.json()
            else:
                logger.error(bstack1ll1l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡤࡱ࡯ࡰࡪࡩࡴࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥ࠳ࠦࡓࡵࡣࡷࡹࡸࡀࠠࡼࡿ࠯ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥᛮ").format(
                    response.status_code, response.text))
                return None
        except Exception as e:
            logger.error(bstack1ll1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡵࡳࡵࡡࡦࡳࡱࡲࡥࡤࡶࡢࡦࡺ࡯࡬ࡥࡡࡧࡥࡹࡧ࠺ࠡࡽࢀࠦᛯ").format(e))
            return None