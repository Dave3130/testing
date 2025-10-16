# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11lll1111l1_opy_
logger = logging.getLogger(__name__)
class bstack11lll11ll11_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack11ll11l1l11_opy_ = urljoin(builder, bstack1ll1ll1_opy_ (u"ࠩ࡬ࡷࡸࡻࡥࡴࠩᚭ"))
        if params:
            bstack11ll11l1l11_opy_ += bstack1ll1ll1_opy_ (u"ࠥࡃࢀࢃࠢᚮ").format(urlencode({bstack1ll1ll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᚯ"): params.get(bstack1ll1ll1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᚰ"))}))
        return bstack11lll11ll11_opy_.bstack11ll11l1l1l_opy_(bstack11ll11l1l11_opy_)
    @staticmethod
    def bstack11ll1l1111l_opy_(builder,params=None):
        bstack11ll11l1l11_opy_ = urljoin(builder, bstack1ll1ll1_opy_ (u"࠭ࡩࡴࡵࡸࡩࡸ࠳ࡳࡶ࡯ࡰࡥࡷࡿࠧᚱ"))
        if params:
            bstack11ll11l1l11_opy_ += bstack1ll1ll1_opy_ (u"ࠢࡀࡽࢀࠦᚲ").format(urlencode({bstack1ll1ll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᚳ"): params.get(bstack1ll1ll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᚴ"))}))
        return bstack11lll11ll11_opy_.bstack11ll11l1l1l_opy_(bstack11ll11l1l11_opy_)
    @staticmethod
    def bstack11ll11l1l1l_opy_(bstack11ll11ll1l1_opy_):
        bstack11ll11ll1ll_opy_ = os.environ.get(bstack1ll1ll1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨᚵ"), os.environ.get(bstack1ll1ll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᚶ"), bstack1ll1ll1_opy_ (u"ࠬ࠭ᚷ")))
        headers = {bstack1ll1ll1_opy_ (u"࠭ࡁࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ᚸ"): bstack1ll1ll1_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪᚹ").format(bstack11ll11ll1ll_opy_)}
        response = requests.get(bstack11ll11ll1l1_opy_, headers=headers)
        bstack11ll11lllll_opy_ = {}
        try:
            bstack11ll11lllll_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣࡎࡘࡕࡎࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠢᚺ").format(e))
            pass
        if bstack11ll11lllll_opy_ is not None:
            bstack11ll11lllll_opy_[bstack1ll1ll1_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᚻ")] = response.headers.get(bstack1ll1ll1_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᚼ"), str(int(datetime.now().timestamp() * 1000)))
            bstack11ll11lllll_opy_[bstack1ll1ll1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᚽ")] = response.status_code
        return bstack11ll11lllll_opy_
    @staticmethod
    def bstack11lll111l11_opy_(bstack11ll11llll1_opy_, data):
        logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡕࡩࡶࡻࡥࡴࡶࠣࡪࡴࡸࠠࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡗࡵࡲࡩࡵࡖࡨࡷࡹࡹࠢᚾ"))
        return bstack11lll11ll11_opy_.bstack11ll11l1ll1_opy_(bstack1ll1ll1_opy_ (u"࠭ࡐࡐࡕࡗࠫᚿ"), bstack11ll11llll1_opy_, data=data)
    @staticmethod
    def bstack11lll111l1l_opy_(bstack11ll11llll1_opy_, data):
        logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡗ࡫ࡱࡶࡧࡶࡸࠥ࡬࡯ࡳࠢࡪࡩࡹ࡚ࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡹࠢᛀ"))
        res = bstack11lll11ll11_opy_.bstack11ll11l1ll1_opy_(bstack1ll1ll1_opy_ (u"ࠨࡉࡈࡘࠬᛁ"), bstack11ll11llll1_opy_, data=data)
        return res
    @staticmethod
    def bstack11ll11l1ll1_opy_(method, bstack11ll11llll1_opy_, data=None, params=None, extra_headers=None):
        bstack11ll11ll1ll_opy_ = os.environ.get(bstack1ll1ll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᛂ"), bstack1ll1ll1_opy_ (u"ࠪࠫᛃ"))
        headers = {
            bstack1ll1ll1_opy_ (u"ࠫࡦࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫᛄ"): bstack1ll1ll1_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥࢁࡽࠨᛅ").format(bstack11ll11ll1ll_opy_),
            bstack1ll1ll1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬᛆ"): bstack1ll1ll1_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪᛇ"),
            bstack1ll1ll1_opy_ (u"ࠨࡃࡦࡧࡪࡶࡴࠨᛈ"): bstack1ll1ll1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬᛉ")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11lll1111l1_opy_ + bstack1ll1ll1_opy_ (u"ࠥ࠳ࠧᛊ") + bstack11ll11llll1_opy_.lstrip(bstack1ll1ll1_opy_ (u"ࠫ࠴࠭ᛋ"))
        try:
            if method == bstack1ll1ll1_opy_ (u"ࠬࡍࡅࡕࠩᛌ"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack1ll1ll1_opy_ (u"࠭ࡐࡐࡕࡗࠫᛍ"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack1ll1ll1_opy_ (u"ࠧࡑࡗࡗࠫᛎ"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack1ll1ll1_opy_ (u"ࠣࡗࡱࡷࡺࡶࡰࡰࡴࡷࡩࡩࠦࡈࡕࡖࡓࠤࡲ࡫ࡴࡩࡱࡧ࠾ࠥࢁࡽࠣᛏ").format(method))
            logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡵࡩࡶࡻࡥࡴࡶࠣࡱࡦࡪࡥࠡࡶࡲࠤ࡚ࡘࡌ࠻ࠢࡾࢁࠥࡽࡩࡵࡪࠣࡱࡪࡺࡨࡰࡦ࠽ࠤࢀࢃࠢᛐ").format(url, method))
            bstack11ll11lllll_opy_ = {}
            try:
                bstack11ll11lllll_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥࡐࡓࡐࡐࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠢ࠰ࠤࢀࢃࠢᛑ").format(e, response.text))
            if bstack11ll11lllll_opy_ is not None:
                bstack11ll11lllll_opy_[bstack1ll1ll1_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬᛒ")] = response.headers.get(
                    bstack1ll1ll1_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭ᛓ"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack11ll11lllll_opy_[bstack1ll1ll1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ᛔ")] = response.status_code
            return bstack11ll11lllll_opy_
        except Exception as e:
            logger.error(bstack1ll1ll1_opy_ (u"ࠢࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡳࡧࡴࡹࡪࡹࡴࠡࡨࡤ࡭ࡱ࡫ࡤ࠻ࠢࡾࢁࠥ࠳ࠠࡼࡿࠥᛕ").format(e, url))
            return None
    @staticmethod
    def bstack11ll11l1lll_opy_(bstack11ll11ll1l1_opy_, data):
        bstack1ll1ll1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤ࡙ࠥࡥ࡯ࡦࡶࠤࡦࠦࡐࡖࡖࠣࡶࡪࡷࡵࡦࡵࡷࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡴࡩࡧࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᛖ")
        bstack11ll11ll1ll_opy_ = os.environ.get(bstack1ll1ll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᛗ"), bstack1ll1ll1_opy_ (u"ࠪࠫᛘ"))
        headers = {
            bstack1ll1ll1_opy_ (u"ࠫࡦࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫᛙ"): bstack1ll1ll1_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥࢁࡽࠨᛚ").format(bstack11ll11ll1ll_opy_),
            bstack1ll1ll1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬᛛ"): bstack1ll1ll1_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪᛜ")
        }
        response = requests.put(bstack11ll11ll1l1_opy_, headers=headers, json=data)
        bstack11ll11lllll_opy_ = {}
        try:
            bstack11ll11lllll_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣࡎࡘࡕࡎࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠢᛝ").format(e))
            pass
        logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡕࡩࡶࡻࡥࡴࡶࡘࡸ࡮ࡲࡳ࠻ࠢࡳࡹࡹࡥࡦࡢ࡫࡯ࡩࡩࡥࡴࡦࡵࡷࡷࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦᛞ").format(bstack11ll11lllll_opy_))
        if bstack11ll11lllll_opy_ is not None:
            bstack11ll11lllll_opy_[bstack1ll1ll1_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᛟ")] = response.headers.get(
                bstack1ll1ll1_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬᛠ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11lllll_opy_[bstack1ll1ll1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᛡ")] = response.status_code
        return bstack11ll11lllll_opy_
    @staticmethod
    def bstack11ll11lll11_opy_(bstack11ll11ll1l1_opy_):
        bstack1ll1ll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡗࡪࡴࡤࡴࠢࡤࠤࡌࡋࡔࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡷࡳࠥ࡭ࡥࡵࠢࡷ࡬ࡪࠦࡣࡰࡷࡱࡸࠥࡵࡦࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᛢ")
        bstack11ll11ll1ll_opy_ = os.environ.get(bstack1ll1ll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᛣ"), bstack1ll1ll1_opy_ (u"ࠨࠩᛤ"))
        headers = {
            bstack1ll1ll1_opy_ (u"ࠩࡤࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩᛥ"): bstack1ll1ll1_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭ᛦ").format(bstack11ll11ll1ll_opy_),
            bstack1ll1ll1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪᛧ"): bstack1ll1ll1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨᛨ")
        }
        response = requests.get(bstack11ll11ll1l1_opy_, headers=headers)
        bstack11ll11lllll_opy_ = {}
        try:
            bstack11ll11lllll_opy_ = response.json()
            logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡒࡦࡳࡸࡩࡸࡺࡕࡵ࡫࡯ࡷ࠿ࠦࡧࡦࡶࡢࡪࡦ࡯࡬ࡦࡦࡢࡸࡪࡹࡴࡴࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠣᛩ").format(bstack11ll11lllll_opy_))
        except Exception as e:
            logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡸࡳࡦࠢࡍࡗࡔࡔࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠦ࠭ࠡࡽࢀࠦᛪ").format(e, response.text))
            pass
        if bstack11ll11lllll_opy_ is not None:
            bstack11ll11lllll_opy_[bstack1ll1ll1_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩ᛫")] = response.headers.get(
                bstack1ll1ll1_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪ᛬"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11lllll_opy_[bstack1ll1ll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ᛭")] = response.status_code
        return bstack11ll11lllll_opy_
    @staticmethod
    def bstack11ll11ll111_opy_(bstack11ll11ll11l_opy_, payload):
        bstack1ll1ll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡏࡤ࡯ࡪࡹࠠࡢࠢࡓࡓࡘ࡚ࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤࡹ࡮ࡥࠡࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡥࡹ࡮ࡲࡤ࠮ࡦࡤࡸࡦࠦࡥ࡯ࡦࡳࡳ࡮ࡴࡴ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡦࡰࡧࡴࡴ࡯࡮ࡵࠢࠫࡷࡹࡸࠩ࠻ࠢࡗ࡬ࡪࠦࡁࡑࡋࠣࡩࡳࡪࡰࡰ࡫ࡱࡸࠥࡶࡡࡵࡪ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡳࡥࡾࡲ࡯ࡢࡦࠣࠬࡩ࡯ࡣࡵࠫ࠽ࠤ࡙࡮ࡥࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡳࡥࡾࡲ࡯ࡢࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡪࡩࡤࡶ࠽ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡦࡳࡱࡰࠤࡹ࡮ࡥࠡࡃࡓࡍ࠱ࠦ࡯ࡳࠢࡑࡳࡳ࡫ࠠࡪࡨࠣࡪࡦ࡯࡬ࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᛮ")
        try:
            url = bstack1ll1ll1_opy_ (u"ࠧࢁࡽ࠰ࡽࢀࠦᛯ").format(bstack11lll1111l1_opy_, bstack11ll11ll11l_opy_)
            bstack11ll11ll1ll_opy_ = os.environ.get(bstack1ll1ll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᛰ"), bstack1ll1ll1_opy_ (u"ࠧࠨᛱ"))
            headers = {
                bstack1ll1ll1_opy_ (u"ࠨࡣࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨᛲ"): bstack1ll1ll1_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬᛳ").format(bstack11ll11ll1ll_opy_),
                bstack1ll1ll1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩᛴ"): bstack1ll1ll1_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧᛵ")
            }
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            bstack11ll11lll1l_opy_ = [200, 202]
            if response.status_code in bstack11ll11lll1l_opy_:
                return response.json()
            else:
                logger.error(bstack1ll1ll1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡥࡲࡰࡱ࡫ࡣࡵࠢࡥࡹ࡮ࡲࡤࠡࡦࡤࡸࡦ࠴ࠠࡔࡶࡤࡸࡺࡹ࠺ࠡࡽࢀ࠰ࠥࡘࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦᛶ").format(
                    response.status_code, response.text))
                return None
        except Exception as e:
            logger.error(bstack1ll1ll1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡯ࡴࡶࡢࡧࡴࡲ࡬ࡦࡥࡷࡣࡧࡻࡩ࡭ࡦࡢࡨࡦࡺࡡ࠻ࠢࡾࢁࠧᛷ").format(e))
            return None