# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11lll11lll1_opy_
logger = logging.getLogger(__name__)
class bstack11lll111111_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack11ll11l1l11_opy_ = urljoin(builder, bstack1lllll1_opy_ (u"ࠧࡪࡵࡶࡹࡪࡹࠧᚫ"))
        if params:
            bstack11ll11l1l11_opy_ += bstack1lllll1_opy_ (u"ࠣࡁࡾࢁࠧᚬ").format(urlencode({bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᚭ"): params.get(bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᚮ"))}))
        return bstack11lll111111_opy_.bstack11ll11ll11l_opy_(bstack11ll11l1l11_opy_)
    @staticmethod
    def bstack11ll1l11l1l_opy_(builder,params=None):
        bstack11ll11l1l11_opy_ = urljoin(builder, bstack1lllll1_opy_ (u"ࠫ࡮ࡹࡳࡶࡧࡶ࠱ࡸࡻ࡭࡮ࡣࡵࡽࠬᚯ"))
        if params:
            bstack11ll11l1l11_opy_ += bstack1lllll1_opy_ (u"ࠧࡅࡻࡾࠤᚰ").format(urlencode({bstack1lllll1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᚱ"): params.get(bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᚲ"))}))
        return bstack11lll111111_opy_.bstack11ll11ll11l_opy_(bstack11ll11l1l11_opy_)
    @staticmethod
    def bstack11ll11ll11l_opy_(bstack11ll11llll1_opy_):
        bstack11ll11ll1ll_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ᚳ"), os.environ.get(bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᚴ"), bstack1lllll1_opy_ (u"ࠪࠫᚵ")))
        headers = {bstack1lllll1_opy_ (u"ࠫࡆࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫᚶ"): bstack1lllll1_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥࢁࡽࠨᚷ").format(bstack11ll11ll1ll_opy_)}
        response = requests.get(bstack11ll11llll1_opy_, headers=headers)
        bstack11ll11l1lll_opy_ = {}
        try:
            bstack11ll11l1lll_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1lllll1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡌࡖࡓࡓࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧᚸ").format(e))
            pass
        if bstack11ll11l1lll_opy_ is not None:
            bstack11ll11l1lll_opy_[bstack1lllll1_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᚹ")] = response.headers.get(bstack1lllll1_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᚺ"), str(int(datetime.now().timestamp() * 1000)))
            bstack11ll11l1lll_opy_[bstack1lllll1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᚻ")] = response.status_code
        return bstack11ll11l1lll_opy_
    @staticmethod
    def bstack11ll1ll1l11_opy_(bstack11ll11ll1l1_opy_, data):
        logger.debug(bstack1lllll1_opy_ (u"ࠥࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡓࡧࡴࡹࡪࡹࡴࠡࡨࡲࡶࠥࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡕࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࠧᚼ"))
        return bstack11lll111111_opy_.bstack11ll11l1l1l_opy_(bstack1lllll1_opy_ (u"ࠫࡕࡕࡓࡕࠩᚽ"), bstack11ll11ll1l1_opy_, data=data)
    @staticmethod
    def bstack11lll111l1l_opy_(bstack11ll11ll1l1_opy_, data):
        logger.debug(bstack1lllll1_opy_ (u"ࠧࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡕࡩࡶࡻࡥࡴࡶࠣࡪࡴࡸࠠࡨࡧࡷࡘࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡷࠧᚾ"))
        res = bstack11lll111111_opy_.bstack11ll11l1l1l_opy_(bstack1lllll1_opy_ (u"࠭ࡇࡆࡖࠪᚿ"), bstack11ll11ll1l1_opy_, data=data)
        return res
    @staticmethod
    def bstack11ll11l1l1l_opy_(method, bstack11ll11ll1l1_opy_, data=None, params=None, extra_headers=None):
        bstack11ll11ll1ll_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᛀ"), bstack1lllll1_opy_ (u"ࠨࠩᛁ"))
        headers = {
            bstack1lllll1_opy_ (u"ࠩࡤࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩᛂ"): bstack1lllll1_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭ᛃ").format(bstack11ll11ll1ll_opy_),
            bstack1lllll1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪᛄ"): bstack1lllll1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨᛅ"),
            bstack1lllll1_opy_ (u"࠭ࡁࡤࡥࡨࡴࡹ࠭ᛆ"): bstack1lllll1_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪᛇ")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11lll11lll1_opy_ + bstack1lllll1_opy_ (u"ࠣ࠱ࠥᛈ") + bstack11ll11ll1l1_opy_.lstrip(bstack1lllll1_opy_ (u"ࠩ࠲ࠫᛉ"))
        try:
            if method == bstack1lllll1_opy_ (u"ࠪࡋࡊ࡚ࠧᛊ"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack1lllll1_opy_ (u"ࠫࡕࡕࡓࡕࠩᛋ"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack1lllll1_opy_ (u"ࠬࡖࡕࡕࠩᛌ"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack1lllll1_opy_ (u"ࠨࡕ࡯ࡵࡸࡴࡵࡵࡲࡵࡧࡧࠤࡍ࡚ࡔࡑࠢࡰࡩࡹ࡮࡯ࡥ࠼ࠣࡿࢂࠨᛍ").format(method))
            logger.debug(bstack1lllll1_opy_ (u"ࠢࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡳࡧࡴࡹࡪࡹࡴࠡ࡯ࡤࡨࡪࠦࡴࡰࠢࡘࡖࡑࡀࠠࡼࡿࠣࡻ࡮ࡺࡨࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠢࡾࢁࠧᛎ").format(url, method))
            bstack11ll11l1lll_opy_ = {}
            try:
                bstack11ll11l1lll_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack1lllll1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣࡎࡘࡕࡎࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠠ࠮ࠢࡾࢁࠧᛏ").format(e, response.text))
            if bstack11ll11l1lll_opy_ is not None:
                bstack11ll11l1lll_opy_[bstack1lllll1_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᛐ")] = response.headers.get(
                    bstack1lllll1_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᛑ"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack11ll11l1lll_opy_[bstack1lllll1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᛒ")] = response.status_code
            return bstack11ll11l1lll_opy_
        except Exception as e:
            logger.error(bstack1lllll1_opy_ (u"ࠧࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡸࡥࡲࡷࡨࡷࡹࠦࡦࡢ࡫࡯ࡩࡩࡀࠠࡼࡿࠣ࠱ࠥࢁࡽࠣᛓ").format(e, url))
            return None
    @staticmethod
    def bstack11ll11lll1l_opy_(bstack11ll11llll1_opy_, data):
        bstack1lllll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡗࡪࡴࡤࡴࠢࡤࠤࡕ࡛ࡔࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡹ࡮ࡥࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᛔ")
        bstack11ll11ll1ll_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᛕ"), bstack1lllll1_opy_ (u"ࠨࠩᛖ"))
        headers = {
            bstack1lllll1_opy_ (u"ࠩࡤࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩᛗ"): bstack1lllll1_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭ᛘ").format(bstack11ll11ll1ll_opy_),
            bstack1lllll1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪᛙ"): bstack1lllll1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨᛚ")
        }
        response = requests.put(bstack11ll11llll1_opy_, headers=headers, json=data)
        bstack11ll11l1lll_opy_ = {}
        try:
            bstack11ll11l1lll_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1lllll1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡌࡖࡓࡓࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧᛛ").format(e))
            pass
        logger.debug(bstack1lllll1_opy_ (u"ࠢࡓࡧࡴࡹࡪࡹࡴࡖࡶ࡬ࡰࡸࡀࠠࡱࡷࡷࡣ࡫ࡧࡩ࡭ࡧࡧࡣࡹ࡫ࡳࡵࡵࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠤᛜ").format(bstack11ll11l1lll_opy_))
        if bstack11ll11l1lll_opy_ is not None:
            bstack11ll11l1lll_opy_[bstack1lllll1_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᛝ")] = response.headers.get(
                bstack1lllll1_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᛞ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11l1lll_opy_[bstack1lllll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᛟ")] = response.status_code
        return bstack11ll11l1lll_opy_
    @staticmethod
    def bstack11ll11lllll_opy_(bstack11ll11llll1_opy_):
        bstack1lllll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡕࡨࡲࡩࡹࠠࡢࠢࡊࡉ࡙ࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣ࡫ࡪࡺࠠࡵࡪࡨࠤࡨࡵࡵ࡯ࡶࠣࡳ࡫ࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᛠ")
        bstack11ll11ll1ll_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩᛡ"), bstack1lllll1_opy_ (u"࠭ࠧᛢ"))
        headers = {
            bstack1lllll1_opy_ (u"ࠧࡢࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧᛣ"): bstack1lllll1_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࡽࢀࠫᛤ").format(bstack11ll11ll1ll_opy_),
            bstack1lllll1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨᛥ"): bstack1lllll1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ᛦ")
        }
        response = requests.get(bstack11ll11llll1_opy_, headers=headers)
        bstack11ll11l1lll_opy_ = {}
        try:
            bstack11ll11l1lll_opy_ = response.json()
            logger.debug(bstack1lllll1_opy_ (u"ࠦࡗ࡫ࡱࡶࡧࡶࡸ࡚ࡺࡩ࡭ࡵ࠽ࠤ࡬࡫ࡴࡠࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨᛧ").format(bstack11ll11l1lll_opy_))
        except Exception as e:
            logger.debug(bstack1lllll1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠤ࠲ࠦࡻࡾࠤᛨ").format(e, response.text))
            pass
        if bstack11ll11l1lll_opy_ is not None:
            bstack11ll11l1lll_opy_[bstack1lllll1_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧᛩ")] = response.headers.get(
                bstack1lllll1_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᛪ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11l1lll_opy_[bstack1lllll1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ᛫")] = response.status_code
        return bstack11ll11l1lll_opy_
    @staticmethod
    def bstack11ll11lll11_opy_(bstack11ll11l1ll1_opy_, payload):
        bstack1lllll1_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡍࡢ࡭ࡨࡷࠥࡧࠠࡑࡑࡖࡘࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡷ࡬ࡪࠦࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡣࡷ࡬ࡰࡩ࠳ࡤࡢࡶࡤࠤࡪࡴࡤࡱࡱ࡬ࡲࡹ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡫࡮ࡥࡲࡲ࡭ࡳࡺࠠࠩࡵࡷࡶ࠮ࡀࠠࡕࡪࡨࠤࡆࡖࡉࠡࡧࡱࡨࡵࡵࡩ࡯ࡶࠣࡴࡦࡺࡨ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡱࡣࡼࡰࡴࡧࡤࠡࠪࡧ࡭ࡨࡺࠩ࠻ࠢࡗ࡬ࡪࠦࡲࡦࡳࡸࡩࡸࡺࠠࡱࡣࡼࡰࡴࡧࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡨ࡮ࡩࡴ࠻ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡁࡑࡋ࠯ࠤࡴࡸࠠࡏࡱࡱࡩࠥ࡯ࡦࠡࡨࡤ࡭ࡱ࡫ࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨ᛬")
        try:
            url = bstack1lllll1_opy_ (u"ࠥࡿࢂ࠵ࡻࡾࠤ᛭").format(bstack11lll11lll1_opy_, bstack11ll11l1ll1_opy_)
            bstack11ll11ll1ll_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᛮ"), bstack1lllll1_opy_ (u"ࠬ࠭ᛯ"))
            headers = {
                bstack1lllll1_opy_ (u"࠭ࡡࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ᛰ"): bstack1lllll1_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪᛱ").format(bstack11ll11ll1ll_opy_),
                bstack1lllll1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧᛲ"): bstack1lllll1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬᛳ")
            }
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            bstack11ll11ll111_opy_ = [200, 202]
            if response.status_code in bstack11ll11ll111_opy_:
                return response.json()
            else:
                logger.error(bstack1lllll1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡣࡰ࡮࡯ࡩࡨࡺࠠࡣࡷ࡬ࡰࡩࠦࡤࡢࡶࡤ࠲࡙ࠥࡴࡢࡶࡸࡷ࠿ࠦࡻࡾ࠮ࠣࡖࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠤᛴ").format(
                    response.status_code, response.text))
                return None
        except Exception as e:
            logger.error(bstack1lllll1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡴࡹࡴࡠࡥࡲࡰࡱ࡫ࡣࡵࡡࡥࡹ࡮ࡲࡤࡠࡦࡤࡸࡦࡀࠠࡼࡿࠥᛵ").format(e))
            return None