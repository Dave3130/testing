# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11ll1llllll_opy_
logger = logging.getLogger(__name__)
class bstack11ll1llll1l_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack11ll11l11l1_opy_ = urljoin(builder, bstack1l1lll1_opy_ (u"ࠩ࡬ࡷࡸࡻࡥࡴࠩᚦ"))
        if params:
            bstack11ll11l11l1_opy_ += bstack1l1lll1_opy_ (u"ࠥࡃࢀࢃࠢᚧ").format(urlencode({bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᚨ"): params.get(bstack1l1lll1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᚩ"))}))
        return bstack11ll1llll1l_opy_.bstack11ll11l11ll_opy_(bstack11ll11l11l1_opy_)
    @staticmethod
    def bstack11ll11lll1l_opy_(builder,params=None):
        bstack11ll11l11l1_opy_ = urljoin(builder, bstack1l1lll1_opy_ (u"࠭ࡩࡴࡵࡸࡩࡸ࠳ࡳࡶ࡯ࡰࡥࡷࡿࠧᚪ"))
        if params:
            bstack11ll11l11l1_opy_ += bstack1l1lll1_opy_ (u"ࠢࡀࡽࢀࠦᚫ").format(urlencode({bstack1l1lll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᚬ"): params.get(bstack1l1lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᚭ"))}))
        return bstack11ll1llll1l_opy_.bstack11ll11l11ll_opy_(bstack11ll11l11l1_opy_)
    @staticmethod
    def bstack11ll11l11ll_opy_(bstack11ll11l1lll_opy_):
        bstack11ll11l1l1l_opy_ = os.environ.get(bstack1l1lll1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨᚮ"), os.environ.get(bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨᚯ"), bstack1l1lll1_opy_ (u"ࠬ࠭ᚰ")))
        headers = {bstack1l1lll1_opy_ (u"࠭ࡁࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ᚱ"): bstack1l1lll1_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪᚲ").format(bstack11ll11l1l1l_opy_)}
        response = requests.get(bstack11ll11l1lll_opy_, headers=headers)
        bstack11ll11l1ll1_opy_ = {}
        try:
            bstack11ll11l1ll1_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1l1lll1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣࡎࡘࡕࡎࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠢᚳ").format(e))
            pass
        if bstack11ll11l1ll1_opy_ is not None:
            bstack11ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᚴ")] = response.headers.get(bstack1l1lll1_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᚵ"), str(int(datetime.now().timestamp() * 1000)))
            bstack11ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫᚶ")] = response.status_code
        return bstack11ll11l1ll1_opy_
    @staticmethod
    def bstack11ll1lll11l_opy_(bstack11ll11ll111_opy_, data):
        logger.debug(bstack1l1lll1_opy_ (u"ࠧࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡕࡩࡶࡻࡥࡴࡶࠣࡪࡴࡸࠠࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡗࡵࡲࡩࡵࡖࡨࡷࡹࡹࠢᚷ"))
        return bstack11ll1llll1l_opy_.bstack11ll11l111l_opy_(bstack1l1lll1_opy_ (u"࠭ࡐࡐࡕࡗࠫᚸ"), bstack11ll11ll111_opy_, data=data)
    @staticmethod
    def bstack11ll1lll1ll_opy_(bstack11ll11ll111_opy_, data):
        logger.debug(bstack1l1lll1_opy_ (u"ࠢࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡗ࡫ࡱࡶࡧࡶࡸࠥ࡬࡯ࡳࠢࡪࡩࡹ࡚ࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡹࠢᚹ"))
        res = bstack11ll1llll1l_opy_.bstack11ll11l111l_opy_(bstack1l1lll1_opy_ (u"ࠨࡉࡈࡘࠬᚺ"), bstack11ll11ll111_opy_, data=data)
        return res
    @staticmethod
    def bstack11ll11l111l_opy_(method, bstack11ll11ll111_opy_, data=None, params=None, extra_headers=None):
        bstack11ll11l1l1l_opy_ = os.environ.get(bstack1l1lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᚻ"), bstack1l1lll1_opy_ (u"ࠪࠫᚼ"))
        headers = {
            bstack1l1lll1_opy_ (u"ࠫࡦࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫᚽ"): bstack1l1lll1_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥࢁࡽࠨᚾ").format(bstack11ll11l1l1l_opy_),
            bstack1l1lll1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬᚿ"): bstack1l1lll1_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪᛀ"),
            bstack1l1lll1_opy_ (u"ࠨࡃࡦࡧࡪࡶࡴࠨᛁ"): bstack1l1lll1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬᛂ")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11ll1llllll_opy_ + bstack1l1lll1_opy_ (u"ࠥ࠳ࠧᛃ") + bstack11ll11ll111_opy_.lstrip(bstack1l1lll1_opy_ (u"ࠫ࠴࠭ᛄ"))
        try:
            if method == bstack1l1lll1_opy_ (u"ࠬࡍࡅࡕࠩᛅ"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack1l1lll1_opy_ (u"࠭ࡐࡐࡕࡗࠫᛆ"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack1l1lll1_opy_ (u"ࠧࡑࡗࡗࠫᛇ"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack1l1lll1_opy_ (u"ࠣࡗࡱࡷࡺࡶࡰࡰࡴࡷࡩࡩࠦࡈࡕࡖࡓࠤࡲ࡫ࡴࡩࡱࡧ࠾ࠥࢁࡽࠣᛈ").format(method))
            logger.debug(bstack1l1lll1_opy_ (u"ࠤࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡵࡩࡶࡻࡥࡴࡶࠣࡱࡦࡪࡥࠡࡶࡲࠤ࡚ࡘࡌ࠻ࠢࡾࢁࠥࡽࡩࡵࡪࠣࡱࡪࡺࡨࡰࡦ࠽ࠤࢀࢃࠢᛉ").format(url, method))
            bstack11ll11l1ll1_opy_ = {}
            try:
                bstack11ll11l1ll1_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack1l1lll1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥࡐࡓࡐࡐࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠢ࠰ࠤࢀࢃࠢᛊ").format(e, response.text))
            if bstack11ll11l1ll1_opy_ is not None:
                bstack11ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬᛋ")] = response.headers.get(
                    bstack1l1lll1_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭ᛌ"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack11ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ᛍ")] = response.status_code
            return bstack11ll11l1ll1_opy_
        except Exception as e:
            logger.error(bstack1l1lll1_opy_ (u"ࠢࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡳࡧࡴࡹࡪࡹࡴࠡࡨࡤ࡭ࡱ࡫ࡤ࠻ࠢࡾࢁࠥ࠳ࠠࡼࡿࠥᛎ").format(e, url))
            return None
    @staticmethod
    def bstack11ll11ll11l_opy_(bstack11ll11l1lll_opy_, data):
        bstack1l1lll1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤ࡙ࠥࡥ࡯ࡦࡶࠤࡦࠦࡐࡖࡖࠣࡶࡪࡷࡵࡦࡵࡷࠤࡹࡵࠠࡴࡶࡲࡶࡪࠦࡴࡩࡧࠣࡪࡦ࡯࡬ࡦࡦࠣࡸࡪࡹࡴࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᛏ")
        bstack11ll11l1l1l_opy_ = os.environ.get(bstack1l1lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ᛐ"), bstack1l1lll1_opy_ (u"ࠪࠫᛑ"))
        headers = {
            bstack1l1lll1_opy_ (u"ࠫࡦࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫᛒ"): bstack1l1lll1_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥࢁࡽࠨᛓ").format(bstack11ll11l1l1l_opy_),
            bstack1l1lll1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬᛔ"): bstack1l1lll1_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪᛕ")
        }
        response = requests.put(bstack11ll11l1lll_opy_, headers=headers, json=data)
        bstack11ll11l1ll1_opy_ = {}
        try:
            bstack11ll11l1ll1_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1l1lll1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣࡎࡘࡕࡎࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠢᛖ").format(e))
            pass
        logger.debug(bstack1l1lll1_opy_ (u"ࠤࡕࡩࡶࡻࡥࡴࡶࡘࡸ࡮ࡲࡳ࠻ࠢࡳࡹࡹࡥࡦࡢ࡫࡯ࡩࡩࡥࡴࡦࡵࡷࡷࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦᛗ").format(bstack11ll11l1ll1_opy_))
        if bstack11ll11l1ll1_opy_ is not None:
            bstack11ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫᛘ")] = response.headers.get(
                bstack1l1lll1_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬᛙ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬᛚ")] = response.status_code
        return bstack11ll11l1ll1_opy_
    @staticmethod
    def bstack11ll11ll1l1_opy_(bstack11ll11l1lll_opy_):
        bstack1l1lll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡗࡪࡴࡤࡴࠢࡤࠤࡌࡋࡔࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡷࡳࠥ࡭ࡥࡵࠢࡷ࡬ࡪࠦࡣࡰࡷࡱࡸࠥࡵࡦࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᛛ")
        bstack11ll11l1l1l_opy_ = os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᛜ"), bstack1l1lll1_opy_ (u"ࠨࠩᛝ"))
        headers = {
            bstack1l1lll1_opy_ (u"ࠩࡤࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩᛞ"): bstack1l1lll1_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭ᛟ").format(bstack11ll11l1l1l_opy_),
            bstack1l1lll1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪᛠ"): bstack1l1lll1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨᛡ")
        }
        response = requests.get(bstack11ll11l1lll_opy_, headers=headers)
        bstack11ll11l1ll1_opy_ = {}
        try:
            bstack11ll11l1ll1_opy_ = response.json()
            logger.debug(bstack1l1lll1_opy_ (u"ࠨࡒࡦࡳࡸࡩࡸࡺࡕࡵ࡫࡯ࡷ࠿ࠦࡧࡦࡶࡢࡪࡦ࡯࡬ࡦࡦࡢࡸࡪࡹࡴࡴࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠣᛢ").format(bstack11ll11l1ll1_opy_))
        except Exception as e:
            logger.debug(bstack1l1lll1_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡸࡳࡦࠢࡍࡗࡔࡔࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠦ࠭ࠡࡽࢀࠦᛣ").format(e, response.text))
            pass
        if bstack11ll11l1ll1_opy_ is not None:
            bstack11ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᛤ")] = response.headers.get(
                bstack1l1lll1_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪᛥ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪᛦ")] = response.status_code
        return bstack11ll11l1ll1_opy_
    @staticmethod
    def bstack11ll11ll1ll_opy_(bstack11ll11l1l11_opy_, payload):
        bstack1l1lll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡏࡤ࡯ࡪࡹࠠࡢࠢࡓࡓࡘ࡚ࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤࡹ࡮ࡥࠡࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡥࡹ࡮ࡲࡤ࠮ࡦࡤࡸࡦࠦࡥ࡯ࡦࡳࡳ࡮ࡴࡴ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡦࡰࡧࡴࡴ࡯࡮ࡵࠢࠫࡷࡹࡸࠩ࠻ࠢࡗ࡬ࡪࠦࡁࡑࡋࠣࡩࡳࡪࡰࡰ࡫ࡱࡸࠥࡶࡡࡵࡪ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡳࡥࡾࡲ࡯ࡢࡦࠣࠬࡩ࡯ࡣࡵࠫ࠽ࠤ࡙࡮ࡥࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡳࡥࡾࡲ࡯ࡢࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡪࡩࡤࡶ࠽ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡦࡳࡱࡰࠤࡹ࡮ࡥࠡࡃࡓࡍ࠱ࠦ࡯ࡳࠢࡑࡳࡳ࡫ࠠࡪࡨࠣࡪࡦ࡯࡬ࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᛧ")
        try:
            url = bstack1l1lll1_opy_ (u"ࠧࢁࡽ࠰ࡽࢀࠦᛨ").format(bstack11ll1llllll_opy_, bstack11ll11l1l11_opy_)
            bstack11ll11l1l1l_opy_ = os.environ.get(bstack1l1lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪᛩ"), bstack1l1lll1_opy_ (u"ࠧࠨᛪ"))
            headers = {
                bstack1l1lll1_opy_ (u"ࠨࡣࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨ᛫"): bstack1l1lll1_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬ᛬").format(bstack11ll11l1l1l_opy_),
                bstack1l1lll1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ᛭"): bstack1l1lll1_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧᛮ")
            }
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            bstack11ll11lll11_opy_ = [200, 202]
            if response.status_code in bstack11ll11lll11_opy_:
                return response.json()
            else:
                logger.error(bstack1l1lll1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡥࡲࡰࡱ࡫ࡣࡵࠢࡥࡹ࡮ࡲࡤࠡࡦࡤࡸࡦ࠴ࠠࡔࡶࡤࡸࡺࡹ࠺ࠡࡽࢀ࠰ࠥࡘࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦᛯ").format(
                    response.status_code, response.text))
                return None
        except Exception as e:
            logger.error(bstack1l1lll1_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡯ࡴࡶࡢࡧࡴࡲ࡬ࡦࡥࡷࡣࡧࡻࡩ࡭ࡦࡢࡨࡦࡺࡡ࠻ࠢࡾࢁࠧᛰ").format(e))
            return None