# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11ll1ll11l1_opy_
logger = logging.getLogger(__name__)
class bstack11ll1ll11ll_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack11ll11l1l11_opy_ = urljoin(builder, bstack11111_opy_ (u"ࠫ࡮ࡹࡳࡶࡧࡶࠫᚚ"))
        if params:
            bstack11ll11l1l11_opy_ += bstack11111_opy_ (u"ࠧࡅࡻࡾࠤ᚛").format(urlencode({bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭᚜"): params.get(bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ᚝"))}))
        return bstack11ll1ll11ll_opy_.bstack11ll11lll11_opy_(bstack11ll11l1l11_opy_)
    @staticmethod
    def bstack11ll1l1111l_opy_(builder,params=None):
        bstack11ll11l1l11_opy_ = urljoin(builder, bstack11111_opy_ (u"ࠨ࡫ࡶࡷࡺ࡫ࡳ࠮ࡵࡸࡱࡲࡧࡲࡺࠩ᚞"))
        if params:
            bstack11ll11l1l11_opy_ += bstack11111_opy_ (u"ࠤࡂࡿࢂࠨ᚟").format(urlencode({bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᚠ"): params.get(bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᚡ"))}))
        return bstack11ll1ll11ll_opy_.bstack11ll11lll11_opy_(bstack11ll11l1l11_opy_)
    @staticmethod
    def bstack11ll11lll11_opy_(bstack11ll11l11l1_opy_):
        bstack11ll11l1ll1_opy_ = os.environ.get(bstack11111_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪᚢ"), os.environ.get(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᚣ"), bstack11111_opy_ (u"ࠧࠨᚤ")))
        headers = {bstack11111_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨᚥ"): bstack11111_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬᚦ").format(bstack11ll11l1ll1_opy_)}
        response = requests.get(bstack11ll11l11l1_opy_, headers=headers)
        bstack11ll11l11ll_opy_ = {}
        try:
            bstack11ll11l11ll_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥࡐࡓࡐࡐࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠤᚧ").format(e))
            pass
        if bstack11ll11l11ll_opy_ is not None:
            bstack11ll11l11ll_opy_[bstack11111_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬᚨ")] = response.headers.get(bstack11111_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭ᚩ"), str(int(datetime.now().timestamp() * 1000)))
            bstack11ll11l11ll_opy_[bstack11111_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ᚪ")] = response.status_code
        return bstack11ll11l11ll_opy_
    @staticmethod
    def bstack11lll111lll_opy_(bstack11ll11l1lll_opy_, data):
        logger.debug(bstack11111_opy_ (u"ࠢࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡗ࡫ࡱࡶࡧࡶࡸࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࡙ࡰ࡭࡫ࡷࡘࡪࡹࡴࡴࠤᚫ"))
        return bstack11ll1ll11ll_opy_.bstack11ll11l111l_opy_(bstack11111_opy_ (u"ࠨࡒࡒࡗ࡙࠭ᚬ"), bstack11ll11l1lll_opy_, data=data)
    @staticmethod
    def bstack11ll1ll111l_opy_(bstack11ll11l1lll_opy_, data):
        logger.debug(bstack11111_opy_ (u"ࠤࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡒࡦࡳࡸࡩࡸࡺࠠࡧࡱࡵࠤ࡬࡫ࡴࡕࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡷࡪࡥࡳࡧࡧࡘࡪࡹࡴࡴࠤᚭ"))
        res = bstack11ll1ll11ll_opy_.bstack11ll11l111l_opy_(bstack11111_opy_ (u"ࠪࡋࡊ࡚ࠧᚮ"), bstack11ll11l1lll_opy_, data=data)
        return res
    @staticmethod
    def bstack11ll11l111l_opy_(method, bstack11ll11l1lll_opy_, data=None, params=None, extra_headers=None):
        bstack11ll11l1ll1_opy_ = os.environ.get(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᚯ"), bstack11111_opy_ (u"ࠬ࠭ᚰ"))
        headers = {
            bstack11111_opy_ (u"࠭ࡡࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ᚱ"): bstack11111_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪᚲ").format(bstack11ll11l1ll1_opy_),
            bstack11111_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧᚳ"): bstack11111_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬᚴ"),
            bstack11111_opy_ (u"ࠪࡅࡨࡩࡥࡱࡶࠪᚵ"): bstack11111_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧᚶ")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11ll1ll11l1_opy_ + bstack11111_opy_ (u"ࠧ࠵ࠢᚷ") + bstack11ll11l1lll_opy_.lstrip(bstack11111_opy_ (u"࠭࠯ࠨᚸ"))
        try:
            if method == bstack11111_opy_ (u"ࠧࡈࡇࡗࠫᚹ"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack11111_opy_ (u"ࠨࡒࡒࡗ࡙࠭ᚺ"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack11111_opy_ (u"ࠩࡓ࡙࡙࠭ᚻ"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack11111_opy_ (u"࡙ࠥࡳࡹࡵࡱࡲࡲࡶࡹ࡫ࡤࠡࡊࡗࡘࡕࠦ࡭ࡦࡶ࡫ࡳࡩࡀࠠࡼࡿࠥᚼ").format(method))
            logger.debug(bstack11111_opy_ (u"ࠦࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡳࡡࡥࡧࠣࡸࡴࠦࡕࡓࡎ࠽ࠤࢀࢃࠠࡸ࡫ࡷ࡬ࠥࡳࡥࡵࡪࡲࡨ࠿ࠦࡻࡾࠤᚽ").format(url, method))
            bstack11ll11l11ll_opy_ = {}
            try:
                bstack11ll11l11ll_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack11111_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠤ࠲ࠦࡻࡾࠤᚾ").format(e, response.text))
            if bstack11ll11l11ll_opy_ is not None:
                bstack11ll11l11ll_opy_[bstack11111_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧᚿ")] = response.headers.get(
                    bstack11111_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᛀ"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack11ll11l11ll_opy_[bstack11111_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᛁ")] = response.status_code
            return bstack11ll11l11ll_opy_
        except Exception as e:
            logger.error(bstack11111_opy_ (u"ࠤࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡵࡩࡶࡻࡥࡴࡶࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࢀࢃࠠ࠮ࠢࡾࢁࠧᛂ").format(e, url))
            return None
    @staticmethod
    def bstack11ll11ll1l1_opy_(bstack11ll11l11l1_opy_, data):
        bstack11111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡔࡧࡱࡨࡸࠦࡡࠡࡒࡘࡘࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡶ࡫ࡩࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡺࡥࡴࡶࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᛃ")
        bstack11ll11l1ll1_opy_ = os.environ.get(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᛄ"), bstack11111_opy_ (u"ࠬ࠭ᛅ"))
        headers = {
            bstack11111_opy_ (u"࠭ࡡࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ᛆ"): bstack11111_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪᛇ").format(bstack11ll11l1ll1_opy_),
            bstack11111_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧᛈ"): bstack11111_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬᛉ")
        }
        response = requests.put(bstack11ll11l11l1_opy_, headers=headers, json=data)
        bstack11ll11l11ll_opy_ = {}
        try:
            bstack11ll11l11ll_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥࡐࡓࡐࡐࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠤᛊ").format(e))
            pass
        logger.debug(bstack11111_opy_ (u"ࠦࡗ࡫ࡱࡶࡧࡶࡸ࡚ࡺࡩ࡭ࡵ࠽ࠤࡵࡻࡴࡠࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨᛋ").format(bstack11ll11l11ll_opy_))
        if bstack11ll11l11ll_opy_ is not None:
            bstack11ll11l11ll_opy_[bstack11111_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭ᛌ")] = response.headers.get(
                bstack11111_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧᛍ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11l11ll_opy_[bstack11111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᛎ")] = response.status_code
        return bstack11ll11l11ll_opy_
    @staticmethod
    def bstack11ll11l1l1l_opy_(bstack11ll11l11l1_opy_):
        bstack11111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤ࡙ࠥࡥ࡯ࡦࡶࠤࡦࠦࡇࡆࡖࠣࡶࡪࡷࡵࡦࡵࡷࠤࡹࡵࠠࡨࡧࡷࠤࡹ࡮ࡥࠡࡥࡲࡹࡳࡺࠠࡰࡨࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᛏ")
        bstack11ll11l1ll1_opy_ = os.environ.get(bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᛐ"), bstack11111_opy_ (u"ࠪࠫᛑ"))
        headers = {
            bstack11111_opy_ (u"ࠫࡦࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫᛒ"): bstack11111_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥࢁࡽࠨᛓ").format(bstack11ll11l1ll1_opy_),
            bstack11111_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬᛔ"): bstack11111_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪᛕ")
        }
        response = requests.get(bstack11ll11l11l1_opy_, headers=headers)
        bstack11ll11l11ll_opy_ = {}
        try:
            bstack11ll11l11ll_opy_ = response.json()
            logger.debug(bstack11111_opy_ (u"ࠣࡔࡨࡵࡺ࡫ࡳࡵࡗࡷ࡭ࡱࡹ࠺ࠡࡩࡨࡸࡤ࡬ࡡࡪ࡮ࡨࡨࡤࡺࡥࡴࡶࡶࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥᛖ").format(bstack11ll11l11ll_opy_))
        except Exception as e:
            logger.debug(bstack11111_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤࡏ࡙ࡏࡏࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠡ࠯ࠣࡿࢂࠨᛗ").format(e, response.text))
            pass
        if bstack11ll11l11ll_opy_ is not None:
            bstack11ll11l11ll_opy_[bstack11111_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᛘ")] = response.headers.get(
                bstack11111_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬᛙ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11l11ll_opy_[bstack11111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᛚ")] = response.status_code
        return bstack11ll11l11ll_opy_
    @staticmethod
    def bstack11ll11ll1ll_opy_(bstack11ll11ll111_opy_, payload):
        bstack11111_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡑࡦࡱࡥࡴࠢࡤࠤࡕࡕࡓࡕࠢࡵࡩࡶࡻࡥࡴࡶࠣࡸࡴࠦࡴࡩࡧࠣࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡧࡻࡩ࡭ࡦ࠰ࡨࡦࡺࡡࠡࡧࡱࡨࡵࡵࡩ࡯ࡶ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡨࡲࡩࡶ࡯ࡪࡰࡷࠤ࠭ࡹࡴࡳࠫ࠽ࠤ࡙࡮ࡥࠡࡃࡓࡍࠥ࡫࡮ࡥࡲࡲ࡭ࡳࡺࠠࡱࡣࡷ࡬࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡵࡧࡹ࡭ࡱࡤࡨࠥ࠮ࡤࡪࡥࡷ࠭࠿ࠦࡔࡩࡧࠣࡶࡪࡷࡵࡦࡵࡷࠤࡵࡧࡹ࡭ࡱࡤࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡥ࡫ࡦࡸ࠿ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡅࡕࡏࠬࠡࡱࡵࠤࡓࡵ࡮ࡦࠢ࡬ࡪࠥ࡬ࡡࡪ࡮ࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᛛ")
        try:
            url = bstack11111_opy_ (u"ࠢࡼࡿ࠲ࡿࢂࠨᛜ").format(bstack11ll1ll11l1_opy_, bstack11ll11ll111_opy_)
            bstack11ll11l1ll1_opy_ = os.environ.get(bstack11111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᛝ"), bstack11111_opy_ (u"ࠩࠪᛞ"))
            headers = {
                bstack11111_opy_ (u"ࠪࡥࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪᛟ"): bstack11111_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧᛠ").format(bstack11ll11l1ll1_opy_),
                bstack11111_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫᛡ"): bstack11111_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩᛢ")
            }
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            bstack11ll11ll11l_opy_ = [200, 202]
            if response.status_code in bstack11ll11ll11l_opy_:
                return response.json()
            else:
                logger.error(bstack11111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡧࡴࡲ࡬ࡦࡥࡷࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡ࠯ࠢࡖࡸࡦࡺࡵࡴ࠼ࠣࡿࢂ࠲ࠠࡓࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨᛣ").format(
                    response.status_code, response.text))
                return None
        except Exception as e:
            logger.error(bstack11111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡱࡶࡸࡤࡩ࡯࡭࡮ࡨࡧࡹࡥࡢࡶ࡫࡯ࡨࡤࡪࡡࡵࡣ࠽ࠤࢀࢃࠢᛤ").format(e))
            return None