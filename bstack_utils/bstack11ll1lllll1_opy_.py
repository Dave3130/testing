# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11lll11111l_opy_
logger = logging.getLogger(__name__)
class bstack11lll111111_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack11ll11l1ll1_opy_ = urljoin(builder, bstack111111l_opy_ (u"ࠪ࡭ࡸࡹࡵࡦࡵࠪᚠ"))
        if params:
            bstack11ll11l1ll1_opy_ += bstack111111l_opy_ (u"ࠦࡄࢁࡽࠣᚡ").format(urlencode({bstack111111l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᚢ"): params.get(bstack111111l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᚣ"))}))
        return bstack11lll111111_opy_.bstack11ll11ll1l1_opy_(bstack11ll11l1ll1_opy_)
    @staticmethod
    def bstack11ll1l11111_opy_(builder,params=None):
        bstack11ll11l1ll1_opy_ = urljoin(builder, bstack111111l_opy_ (u"ࠧࡪࡵࡶࡹࡪࡹ࠭ࡴࡷࡰࡱࡦࡸࡹࠨᚤ"))
        if params:
            bstack11ll11l1ll1_opy_ += bstack111111l_opy_ (u"ࠣࡁࡾࢁࠧᚥ").format(urlencode({bstack111111l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᚦ"): params.get(bstack111111l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᚧ"))}))
        return bstack11lll111111_opy_.bstack11ll11ll1l1_opy_(bstack11ll11l1ll1_opy_)
    @staticmethod
    def bstack11ll11ll1l1_opy_(bstack11ll11l1l1l_opy_):
        bstack11ll11l11ll_opy_ = os.environ.get(bstack111111l_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩᚨ"), os.environ.get(bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩᚩ"), bstack111111l_opy_ (u"࠭ࠧᚪ")))
        headers = {bstack111111l_opy_ (u"ࠧࡂࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧᚫ"): bstack111111l_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࡽࢀࠫᚬ").format(bstack11ll11l11ll_opy_)}
        response = requests.get(bstack11ll11l1l1l_opy_, headers=headers)
        bstack11ll11l1l11_opy_ = {}
        try:
            bstack11ll11l1l11_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack111111l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤࡏ࡙ࡏࡏࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠣᚭ").format(e))
            pass
        if bstack11ll11l1l11_opy_ is not None:
            bstack11ll11l1l11_opy_[bstack111111l_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᚮ")] = response.headers.get(bstack111111l_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬᚯ"), str(int(datetime.now().timestamp() * 1000)))
            bstack11ll11l1l11_opy_[bstack111111l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᚰ")] = response.status_code
        return bstack11ll11l1l11_opy_
    @staticmethod
    def bstack11ll1llllll_opy_(bstack11ll11l11l1_opy_, data):
        logger.debug(bstack111111l_opy_ (u"ࠨࡐࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡖࡪࡷࡵࡦࡵࡷࠤ࡫ࡵࡲࠡࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡘࡶ࡬ࡪࡶࡗࡩࡸࡺࡳࠣᚱ"))
        return bstack11lll111111_opy_.bstack11ll11l1lll_opy_(bstack111111l_opy_ (u"ࠧࡑࡑࡖࡘࠬᚲ"), bstack11ll11l11l1_opy_, data=data)
    @staticmethod
    def bstack11lll1111ll_opy_(bstack11ll11l11l1_opy_, data):
        logger.debug(bstack111111l_opy_ (u"ࠣࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡘࡥࡲࡷࡨࡷࡹࠦࡦࡰࡴࠣ࡫ࡪࡺࡔࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡶࡩ࡫ࡲࡦࡦࡗࡩࡸࡺࡳࠣᚳ"))
        res = bstack11lll111111_opy_.bstack11ll11l1lll_opy_(bstack111111l_opy_ (u"ࠩࡊࡉ࡙࠭ᚴ"), bstack11ll11l11l1_opy_, data=data)
        return res
    @staticmethod
    def bstack11ll11l1lll_opy_(method, bstack11ll11l11l1_opy_, data=None, params=None, extra_headers=None):
        bstack11ll11l11ll_opy_ = os.environ.get(bstack111111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧᚵ"), bstack111111l_opy_ (u"ࠫࠬᚶ"))
        headers = {
            bstack111111l_opy_ (u"ࠬࡧࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲࠬᚷ"): bstack111111l_opy_ (u"࠭ࡂࡦࡣࡵࡩࡷࠦࡻࡾࠩᚸ").format(bstack11ll11l11ll_opy_),
            bstack111111l_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭ᚹ"): bstack111111l_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫᚺ"),
            bstack111111l_opy_ (u"ࠩࡄࡧࡨ࡫ࡰࡵࠩᚻ"): bstack111111l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ᚼ")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11lll11111l_opy_ + bstack111111l_opy_ (u"ࠦ࠴ࠨᚽ") + bstack11ll11l11l1_opy_.lstrip(bstack111111l_opy_ (u"ࠬ࠵ࠧᚾ"))
        try:
            if method == bstack111111l_opy_ (u"࠭ࡇࡆࡖࠪᚿ"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack111111l_opy_ (u"ࠧࡑࡑࡖࡘࠬᛀ"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack111111l_opy_ (u"ࠨࡒࡘࡘࠬᛁ"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack111111l_opy_ (u"ࠤࡘࡲࡸࡻࡰࡱࡱࡵࡸࡪࡪࠠࡉࡖࡗࡔࠥࡳࡥࡵࡪࡲࡨ࠿ࠦࡻࡾࠤᛂ").format(method))
            logger.debug(bstack111111l_opy_ (u"ࠥࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡶࡪࡷࡵࡦࡵࡷࠤࡲࡧࡤࡦࠢࡷࡳ࡛ࠥࡒࡍ࠼ࠣࡿࢂࠦࡷࡪࡶ࡫ࠤࡲ࡫ࡴࡩࡱࡧ࠾ࠥࢁࡽࠣᛃ").format(url, method))
            bstack11ll11l1l11_opy_ = {}
            try:
                bstack11ll11l1l11_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack111111l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡊࡔࡑࡑࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠣ࠱ࠥࢁࡽࠣᛄ").format(e, response.text))
            if bstack11ll11l1l11_opy_ is not None:
                bstack11ll11l1l11_opy_[bstack111111l_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭ᛅ")] = response.headers.get(
                    bstack111111l_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧᛆ"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack11ll11l1l11_opy_[bstack111111l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᛇ")] = response.status_code
            return bstack11ll11l1l11_opy_
        except Exception as e:
            logger.error(bstack111111l_opy_ (u"ࠣࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࡿࢂࠦ࠭ࠡࡽࢀࠦᛈ").format(e, url))
            return None
    @staticmethod
    def bstack11ll11ll1ll_opy_(bstack11ll11l1l1l_opy_, data):
        bstack111111l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡓࡦࡰࡧࡷࠥࡧࠠࡑࡗࡗࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡺ࡯ࠡࡵࡷࡳࡷ࡫ࠠࡵࡪࡨࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᛉ")
        bstack11ll11l11ll_opy_ = os.environ.get(bstack111111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧᛊ"), bstack111111l_opy_ (u"ࠫࠬᛋ"))
        headers = {
            bstack111111l_opy_ (u"ࠬࡧࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲࠬᛌ"): bstack111111l_opy_ (u"࠭ࡂࡦࡣࡵࡩࡷࠦࡻࡾࠩᛍ").format(bstack11ll11l11ll_opy_),
            bstack111111l_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭ᛎ"): bstack111111l_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫᛏ")
        }
        response = requests.put(bstack11ll11l1l1l_opy_, headers=headers, json=data)
        bstack11ll11l1l11_opy_ = {}
        try:
            bstack11ll11l1l11_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack111111l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤࡏ࡙ࡏࡏࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠣᛐ").format(e))
            pass
        logger.debug(bstack111111l_opy_ (u"ࠥࡖࡪࡷࡵࡦࡵࡷ࡙ࡹ࡯࡬ࡴ࠼ࠣࡴࡺࡺ࡟ࡧࡣ࡬ࡰࡪࡪ࡟ࡵࡧࡶࡸࡸࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧᛑ").format(bstack11ll11l1l11_opy_))
        if bstack11ll11l1l11_opy_ is not None:
            bstack11ll11l1l11_opy_[bstack111111l_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬᛒ")] = response.headers.get(
                bstack111111l_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭ᛓ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11l1l11_opy_[bstack111111l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ᛔ")] = response.status_code
        return bstack11ll11l1l11_opy_
    @staticmethod
    def bstack11ll11lll11_opy_(bstack11ll11l1l1l_opy_):
        bstack111111l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡘ࡫࡮ࡥࡵࠣࡥࠥࡍࡅࡕࠢࡵࡩࡶࡻࡥࡴࡶࠣࡸࡴࠦࡧࡦࡶࠣࡸ࡭࡫ࠠࡤࡱࡸࡲࡹࠦ࡯ࡧࠢࡩࡥ࡮ࡲࡥࡥࠢࡷࡩࡸࡺࡳࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᛕ")
        bstack11ll11l11ll_opy_ = os.environ.get(bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬᛖ"), bstack111111l_opy_ (u"ࠩࠪᛗ"))
        headers = {
            bstack111111l_opy_ (u"ࠪࡥࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪᛘ"): bstack111111l_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧᛙ").format(bstack11ll11l11ll_opy_),
            bstack111111l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫᛚ"): bstack111111l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩᛛ")
        }
        response = requests.get(bstack11ll11l1l1l_opy_, headers=headers)
        bstack11ll11l1l11_opy_ = {}
        try:
            bstack11ll11l1l11_opy_ = response.json()
            logger.debug(bstack111111l_opy_ (u"ࠢࡓࡧࡴࡹࡪࡹࡴࡖࡶ࡬ࡰࡸࡀࠠࡨࡧࡷࡣ࡫ࡧࡩ࡭ࡧࡧࡣࡹ࡫ࡳࡵࡵࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠤᛜ").format(bstack11ll11l1l11_opy_))
        except Exception as e:
            logger.debug(bstack111111l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣࡎࡘࡕࡎࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠠ࠮ࠢࡾࢁࠧᛝ").format(e, response.text))
            pass
        if bstack11ll11l1l11_opy_ is not None:
            bstack11ll11l1l11_opy_[bstack111111l_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᛞ")] = response.headers.get(
                bstack111111l_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᛟ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11l1l11_opy_[bstack111111l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᛠ")] = response.status_code
        return bstack11ll11l1l11_opy_
    @staticmethod
    def bstack11ll11ll11l_opy_(bstack11ll11ll111_opy_, payload):
        bstack111111l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡐࡥࡰ࡫ࡳࠡࡣࠣࡔࡔ࡙ࡔࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡷࡳࠥࡺࡨࡦࠢࡦࡳࡱࡲࡥࡤࡶ࠰ࡦࡺ࡯࡬ࡥ࠯ࡧࡥࡹࡧࠠࡦࡰࡧࡴࡴ࡯࡮ࡵ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡆࡸࡧࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡧࡱࡨࡵࡵࡩ࡯ࡶࠣࠬࡸࡺࡲࠪ࠼ࠣࡘ࡭࡫ࠠࡂࡒࡌࠤࡪࡴࡤࡱࡱ࡬ࡲࡹࠦࡰࡢࡶ࡫࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡴࡦࡿ࡬ࡰࡣࡧࠤ࠭ࡪࡩࡤࡶࠬ࠾࡚ࠥࡨࡦࠢࡵࡩࡶࡻࡥࡴࡶࠣࡴࡦࡿ࡬ࡰࡣࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡤࡪࡥࡷ࠾ࠥࡘࡥࡴࡲࡲࡲࡸ࡫ࠠࡧࡴࡲࡱࠥࡺࡨࡦࠢࡄࡔࡎ࠲ࠠࡰࡴࠣࡒࡴࡴࡥࠡ࡫ࡩࠤ࡫ࡧࡩ࡭ࡧࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᛡ")
        try:
            url = bstack111111l_opy_ (u"ࠨࡻࡾ࠱ࡾࢁࠧᛢ").format(bstack11lll11111l_opy_, bstack11ll11ll111_opy_)
            bstack11ll11l11ll_opy_ = os.environ.get(bstack111111l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᛣ"), bstack111111l_opy_ (u"ࠨࠩᛤ"))
            headers = {
                bstack111111l_opy_ (u"ࠩࡤࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩᛥ"): bstack111111l_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭ᛦ").format(bstack11ll11l11ll_opy_),
                bstack111111l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪᛧ"): bstack111111l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨᛨ")
            }
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            bstack11ll11lll1l_opy_ = [200, 202]
            if response.status_code in bstack11ll11lll1l_opy_:
                return response.json()
            else:
                logger.error(bstack111111l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡦࡳࡱࡲࡥࡤࡶࠣࡦࡺ࡯࡬ࡥࠢࡧࡥࡹࡧ࠮ࠡࡕࡷࡥࡹࡻࡳ࠻ࠢࡾࢁ࠱ࠦࡒࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧᛩ").format(
                    response.status_code, response.text))
                return None
        except Exception as e:
            logger.error(bstack111111l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡰࡵࡷࡣࡨࡵ࡬࡭ࡧࡦࡸࡤࡨࡵࡪ࡮ࡧࡣࡩࡧࡴࡢ࠼ࠣࡿࢂࠨᛪ").format(e))
            return None