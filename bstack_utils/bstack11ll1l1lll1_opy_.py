# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11ll1ll1111_opy_
logger = logging.getLogger(__name__)
class bstack11ll1l1ll11_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack11ll1111lll_opy_ = urljoin(builder, bstack11ll1l_opy_ (u"ࠬ࡯ࡳࡴࡷࡨࡷࠬᛚ"))
        if params:
            bstack11ll1111lll_opy_ += bstack11ll1l_opy_ (u"ࠨ࠿ࡼࡿࠥᛛ").format(urlencode({bstack11ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᛜ"): params.get(bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᛝ"))}))
        return bstack11ll1l1ll11_opy_.bstack11ll111l111_opy_(bstack11ll1111lll_opy_)
    @staticmethod
    def bstack11ll11l11l1_opy_(builder,params=None):
        bstack11ll1111lll_opy_ = urljoin(builder, bstack11ll1l_opy_ (u"ࠩ࡬ࡷࡸࡻࡥࡴ࠯ࡶࡹࡲࡳࡡࡳࡻࠪᛞ"))
        if params:
            bstack11ll1111lll_opy_ += bstack11ll1l_opy_ (u"ࠥࡃࢀࢃࠢᛟ").format(urlencode({bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᛠ"): params.get(bstack11ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬᛡ"))}))
        return bstack11ll1l1ll11_opy_.bstack11ll111l111_opy_(bstack11ll1111lll_opy_)
    @staticmethod
    def bstack11ll111l111_opy_(bstack11ll111lll1_opy_):
        bstack11ll111l1l1_opy_ = os.environ.get(bstack11ll1l_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫᛢ"), os.environ.get(bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᛣ"), bstack11ll1l_opy_ (u"ࠨࠩᛤ")))
        headers = {bstack11ll1l_opy_ (u"ࠩࡄࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩᛥ"): bstack11ll1l_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭ᛦ").format(bstack11ll111l1l1_opy_)}
        response = requests.get(bstack11ll111lll1_opy_, headers=headers)
        bstack11ll1111l1l_opy_ = {}
        try:
            bstack11ll1111l1l_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack11ll1l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡊࡔࡑࡑࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥᛧ").format(e))
            pass
        if bstack11ll1111l1l_opy_ is not None:
            bstack11ll1111l1l_opy_[bstack11ll1l_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭ᛨ")] = response.headers.get(bstack11ll1l_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧᛩ"), str(int(datetime.now().timestamp() * 1000)))
            bstack11ll1111l1l_opy_[bstack11ll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᛪ")] = response.status_code
        return bstack11ll1111l1l_opy_
    @staticmethod
    def bstack11ll1llll11_opy_(bstack11ll111l1ll_opy_, data):
        logger.debug(bstack11ll1l_opy_ (u"ࠣࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡘࡥࡲࡷࡨࡷࡹࠦࡦࡰࡴࠣࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡓࡱ࡮࡬ࡸ࡙࡫ࡳࡵࡵࠥ᛫"))
        return bstack11ll1l1ll11_opy_.bstack11ll111ll1l_opy_(bstack11ll1l_opy_ (u"ࠩࡓࡓࡘ࡚ࠧ᛬"), bstack11ll111l1ll_opy_, data=data)
    @staticmethod
    def bstack11ll1lll111_opy_(bstack11ll111l1ll_opy_, data):
        logger.debug(bstack11ll1l_opy_ (u"ࠥࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡓࡧࡴࡹࡪࡹࡴࠡࡨࡲࡶࠥ࡭ࡥࡵࡖࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡸࡤࡦࡴࡨࡨ࡙࡫ࡳࡵࡵࠥ᛭"))
        res = bstack11ll1l1ll11_opy_.bstack11ll111ll1l_opy_(bstack11ll1l_opy_ (u"ࠫࡌࡋࡔࠨᛮ"), bstack11ll111l1ll_opy_, data=data)
        return res
    @staticmethod
    def bstack11ll111ll1l_opy_(method, bstack11ll111l1ll_opy_, data=None, params=None, extra_headers=None):
        bstack11ll111l1l1_opy_ = os.environ.get(bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩᛯ"), bstack11ll1l_opy_ (u"࠭ࠧᛰ"))
        headers = {
            bstack11ll1l_opy_ (u"ࠧࡢࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧᛱ"): bstack11ll1l_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࡽࢀࠫᛲ").format(bstack11ll111l1l1_opy_),
            bstack11ll1l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨᛳ"): bstack11ll1l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ᛴ"),
            bstack11ll1l_opy_ (u"ࠫࡆࡩࡣࡦࡲࡷࠫᛵ"): bstack11ll1l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨᛶ")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11ll1ll1111_opy_ + bstack11ll1l_opy_ (u"ࠨ࠯ࠣᛷ") + bstack11ll111l1ll_opy_.lstrip(bstack11ll1l_opy_ (u"ࠧ࠰ࠩᛸ"))
        try:
            if method == bstack11ll1l_opy_ (u"ࠨࡉࡈࡘࠬ᛹"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack11ll1l_opy_ (u"ࠩࡓࡓࡘ࡚ࠧ᛺"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack11ll1l_opy_ (u"ࠪࡔ࡚࡚ࠧ᛻"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack11ll1l_opy_ (u"࡚ࠦࡴࡳࡶࡲࡳࡳࡷࡺࡥࡥࠢࡋࡘ࡙ࡖࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠡࡽࢀࠦ᛼").format(method))
            logger.debug(bstack11ll1l_opy_ (u"ࠧࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡸࡥࡲࡷࡨࡷࡹࠦ࡭ࡢࡦࡨࠤࡹࡵࠠࡖࡔࡏ࠾ࠥࢁࡽࠡࡹ࡬ࡸ࡭ࠦ࡭ࡦࡶ࡫ࡳࡩࡀࠠࡼࡿࠥ᛽").format(url, method))
            bstack11ll1111l1l_opy_ = {}
            try:
                bstack11ll1111l1l_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack11ll1l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡌࡖࡓࡓࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠥ࠳ࠠࡼࡿࠥ᛾").format(e, response.text))
            if bstack11ll1111l1l_opy_ is not None:
                bstack11ll1111l1l_opy_[bstack11ll1l_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨ᛿")] = response.headers.get(
                    bstack11ll1l_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩᜀ"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack11ll1111l1l_opy_[bstack11ll1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩᜁ")] = response.status_code
            return bstack11ll1111l1l_opy_
        except Exception as e:
            logger.error(bstack11ll1l_opy_ (u"ࠥࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡶࡪࡷࡵࡦࡵࡷࠤ࡫ࡧࡩ࡭ࡧࡧ࠾ࠥࢁࡽࠡ࠯ࠣࡿࢂࠨᜂ").format(e, url))
            return None
    @staticmethod
    def bstack11ll1111ll1_opy_(bstack11ll111lll1_opy_, data):
        bstack11ll1l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡕࡨࡲࡩࡹࠠࡢࠢࡓ࡙࡙ࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣࡷࡹࡵࡲࡦࠢࡷ࡬ࡪࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᜃ")
        bstack11ll111l1l1_opy_ = os.environ.get(bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩᜄ"), bstack11ll1l_opy_ (u"࠭ࠧᜅ"))
        headers = {
            bstack11ll1l_opy_ (u"ࠧࡢࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧᜆ"): bstack11ll1l_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࡽࢀࠫᜇ").format(bstack11ll111l1l1_opy_),
            bstack11ll1l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨᜈ"): bstack11ll1l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ᜉ")
        }
        response = requests.put(bstack11ll111lll1_opy_, headers=headers, json=data)
        bstack11ll1111l1l_opy_ = {}
        try:
            bstack11ll1111l1l_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack11ll1l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡊࡔࡑࡑࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥᜊ").format(e))
            pass
        logger.debug(bstack11ll1l_opy_ (u"ࠧࡘࡥࡲࡷࡨࡷࡹ࡛ࡴࡪ࡮ࡶ࠾ࠥࡶࡵࡵࡡࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠢᜋ").format(bstack11ll1111l1l_opy_))
        if bstack11ll1111l1l_opy_ is not None:
            bstack11ll1111l1l_opy_[bstack11ll1l_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧᜌ")] = response.headers.get(
                bstack11ll1l_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨᜍ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll1111l1l_opy_[bstack11ll1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᜎ")] = response.status_code
        return bstack11ll1111l1l_opy_
    @staticmethod
    def bstack11ll111llll_opy_(bstack11ll111lll1_opy_):
        bstack11ll1l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡓࡦࡰࡧࡷࠥࡧࠠࡈࡇࡗࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡺ࡯ࠡࡩࡨࡸࠥࡺࡨࡦࠢࡦࡳࡺࡴࡴࠡࡱࡩࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹ࡫ࡳࡵࡵࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᜏ")
        bstack11ll111l1l1_opy_ = os.environ.get(bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧᜐ"), bstack11ll1l_opy_ (u"ࠫࠬᜑ"))
        headers = {
            bstack11ll1l_opy_ (u"ࠬࡧࡵࡵࡪࡲࡶ࡮ࢀࡡࡵ࡫ࡲࡲࠬᜒ"): bstack11ll1l_opy_ (u"࠭ࡂࡦࡣࡵࡩࡷࠦࡻࡾࠩᜓ").format(bstack11ll111l1l1_opy_),
            bstack11ll1l_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ᜔࠭"): bstack11ll1l_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱ᜕ࠫ")
        }
        response = requests.get(bstack11ll111lll1_opy_, headers=headers)
        bstack11ll1111l1l_opy_ = {}
        try:
            bstack11ll1111l1l_opy_ = response.json()
            logger.debug(bstack11ll1l_opy_ (u"ࠤࡕࡩࡶࡻࡥࡴࡶࡘࡸ࡮ࡲࡳ࠻ࠢࡪࡩࡹࡥࡦࡢ࡫࡯ࡩࡩࡥࡴࡦࡵࡷࡷࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦ᜖").format(bstack11ll1111l1l_opy_))
        except Exception as e:
            logger.debug(bstack11ll1l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥࡐࡓࡐࡐࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠢ࠰ࠤࢀࢃࠢ᜗").format(e, response.text))
            pass
        if bstack11ll1111l1l_opy_ is not None:
            bstack11ll1111l1l_opy_[bstack11ll1l_opy_ (u"ࠫࡳ࡫ࡸࡵࡡࡳࡳࡱࡲ࡟ࡵ࡫ࡰࡩࠬ᜘")] = response.headers.get(
                bstack11ll1l_opy_ (u"ࠬࡴࡥࡹࡶࡢࡴࡴࡲ࡬ࡠࡶ࡬ࡱࡪ࠭᜙"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack11ll1111l1l_opy_[bstack11ll1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭᜚")] = response.status_code
        return bstack11ll1111l1l_opy_
    @staticmethod
    def bstack11ll111ll11_opy_(bstack11ll111l11l_opy_, payload):
        bstack11ll1l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡒࡧ࡫ࡦࡵࠣࡥࠥࡖࡏࡔࡖࠣࡶࡪࡷࡵࡦࡵࡷࠤࡹࡵࠠࡵࡪࡨࠤࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡨࡵࡪ࡮ࡧ࠱ࡩࡧࡴࡢࠢࡨࡲࡩࡶ࡯ࡪࡰࡷ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡁࡳࡩࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡩࡳࡪࡰࡰ࡫ࡱࡸࠥ࠮ࡳࡵࡴࠬ࠾࡚ࠥࡨࡦࠢࡄࡔࡎࠦࡥ࡯ࡦࡳࡳ࡮ࡴࡴࠡࡲࡤࡸ࡭࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡶࡡࡺ࡮ࡲࡥࡩࠦࠨࡥ࡫ࡦࡸ࠮ࡀࠠࡕࡪࡨࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡶࡡࡺ࡮ࡲࡥࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡦ࡬ࡧࡹࡀࠠࡓࡧࡶࡴࡴࡴࡳࡦࠢࡩࡶࡴࡳࠠࡵࡪࡨࠤࡆࡖࡉ࠭ࠢࡲࡶࠥࡔ࡯࡯ࡧࠣ࡭࡫ࠦࡦࡢ࡫࡯ࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ᜛")
        try:
            url = bstack11ll1l_opy_ (u"ࠣࡽࢀ࠳ࢀࢃࠢ᜜").format(bstack11ll1ll1111_opy_, bstack11ll111l11l_opy_)
            bstack11ll111l1l1_opy_ = os.environ.get(bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭᜝"), bstack11ll1l_opy_ (u"ࠪࠫ᜞"))
            headers = {
                bstack11ll1l_opy_ (u"ࠫࡦࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫᜟ"): bstack11ll1l_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥࢁࡽࠨᜠ").format(bstack11ll111l1l1_opy_),
                bstack11ll1l_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬᜡ"): bstack11ll1l_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪᜢ")
            }
            response = requests.post(url, json=payload, headers=headers, timeout=30)
            bstack11ll11l1111_opy_ = [200, 202]
            if response.status_code in bstack11ll11l1111_opy_:
                return response.json()
            else:
                logger.error(bstack11ll1l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡨࡵ࡬࡭ࡧࡦࡸࠥࡨࡵࡪ࡮ࡧࠤࡩࡧࡴࡢ࠰ࠣࡗࡹࡧࡴࡶࡵ࠽ࠤࢀࢃࠬࠡࡔࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠢᜣ").format(
                    response.status_code, response.text))
                return None
        except Exception as e:
            logger.error(bstack11ll1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡲࡷࡹࡥࡣࡰ࡮࡯ࡩࡨࡺ࡟ࡣࡷ࡬ࡰࡩࡥࡤࡢࡶࡤ࠾ࠥࢁࡽࠣᜤ").format(e))
            return None