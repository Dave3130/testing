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
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111l11l11l1_opy_, bstack111l11ll11l_opy_, bstack1l11lllll_opy_, error_handler, bstack1111lllllll_opy_, bstack111l11ll1ll_opy_, bstack1111ll1l1l1_opy_, bstack1l1l1lll_opy_, bstack1l1l1l1l_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l11l1lll1_opy_ import bstack111ll111ll1_opy_
import bstack_utils.bstack111l111l1_opy_ as bstack1l11lll111_opy_
from bstack_utils.bstack11llll1l_opy_ import bstack1l11llll_opy_
import bstack_utils.accessibility as bstack1lllllll1_opy_
from bstack_utils.bstack1l1ll1lll1_opy_ import bstack1l1ll1lll1_opy_
from bstack_utils.bstack1l1l1ll1_opy_ import bstack1ll1llll_opy_
from bstack_utils.constants import bstack1l11l11ll1_opy_
bstack1llll1l1l1l1_opy_ = bstack1ll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡩ࡯࡭࡮ࡨࡧࡹࡵࡲ࠮ࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫ⃷")
logger = logging.getLogger(__name__)
class bstack1lllll11_opy_:
    bstack11l11l1lll1_opy_ = None
    bs_config = None
    bstack1lll11ll1l_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l1l1l1lll_opy_, stage=STAGE.bstack11lll11ll_opy_)
    def launch(cls, bs_config, bstack1lll11ll1l_opy_):
        cls.bs_config = bs_config
        cls.bstack1lll11ll1l_opy_ = bstack1lll11ll1l_opy_
        try:
            cls.bstack1llll11llll1_opy_()
            bstack1lllll11l11l_opy_ = bstack111l11l11l1_opy_(bs_config)
            bstack1llll1lll111_opy_ = bstack111l11ll11l_opy_(bs_config)
            data = bstack1l11lll111_opy_.bstack1llll1l1111l_opy_(bs_config, bstack1lll11ll1l_opy_)
            config = {
                bstack1ll1l_opy_ (u"ࠬࡧࡵࡵࡪࠪ⃸"): (bstack1lllll11l11l_opy_, bstack1llll1lll111_opy_),
                bstack1ll1l_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ⃹"): cls.default_headers()
            }
            response = bstack1l11lllll_opy_(bstack1ll1l_opy_ (u"ࠧࡑࡑࡖࡘࠬ⃺"), cls.request_url(bstack1ll1l_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠲࠰ࡤࡸ࡭ࡱࡪࡳࠨ⃻")), data, config)
            if response.status_code != 200:
                bstack1ll1l1lll_opy_ = response.json()
                if bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ⃼")] == False:
                    cls.bstack1llll1ll111l_opy_(bstack1ll1l1lll_opy_)
                    return
                cls.bstack1llll11lll11_opy_(bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ⃽")])
                cls.bstack1llll1l11l11_opy_(bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⃾")])
                return None
            bstack1llll1ll1111_opy_ = cls.bstack1llll1l1lll1_opy_(response)
            return bstack1llll1ll1111_opy_, response.json()
        except Exception as error:
            logger.error(bstack1ll1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡥࡹ࡮ࡲࡤࠡࡨࡲࡶ࡚ࠥࡥࡴࡶࡋࡹࡧࡀࠠࡼࡿࠥ⃿").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll1l1llll_opy_=None):
        if not bstack1l11llll_opy_.on() and not bstack1lllllll1_opy_.on():
            return
        if os.environ.get(bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ℀")) == bstack1ll1l_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ℁") or os.environ.get(bstack1ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ℂ")) == bstack1ll1l_opy_ (u"ࠤࡱࡹࡱࡲࠢ℃"):
            logger.error(bstack1ll1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡴࡶࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡡࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷ࡭ࡴࡴࠠࡵࡱ࡮ࡩࡳ࠭℄"))
            return {
                bstack1ll1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ℅"): bstack1ll1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ℆"),
                bstack1ll1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧℇ"): bstack1ll1l_opy_ (u"ࠧࡕࡱ࡮ࡩࡳ࠵ࡢࡶ࡫࡯ࡨࡎࡊࠠࡪࡵࠣࡹࡳࡪࡥࡧ࡫ࡱࡩࡩ࠲ࠠࡣࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡ࡯࡬࡫࡭ࡺࠠࡩࡣࡹࡩࠥ࡬ࡡࡪ࡮ࡨࡨࠬ℈")
            }
        try:
            cls.bstack11l11l1lll1_opy_.shutdown()
            data = {
                bstack1ll1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭℉"): bstack1l1l1lll_opy_()
            }
            if not bstack1llll1l1llll_opy_ is None:
                data[bstack1ll1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡲ࡫ࡴࡢࡦࡤࡸࡦ࠭ℊ")] = [{
                    bstack1ll1l_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪℋ"): bstack1ll1l_opy_ (u"ࠫࡺࡹࡥࡳࡡ࡮࡭ࡱࡲࡥࡥࠩℌ"),
                    bstack1ll1l_opy_ (u"ࠬࡹࡩࡨࡰࡤࡰࠬℍ"): bstack1llll1l1llll_opy_
                }]
            config = {
                bstack1ll1l_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧℎ"): cls.default_headers()
            }
            bstack11ll11l1lll_opy_ = bstack1ll1l_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡷࡹࡵࡰࠨℏ").format(os.environ[bstack1ll1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨℐ")])
            bstack1llll1l11l1l_opy_ = cls.request_url(bstack11ll11l1lll_opy_)
            response = bstack1l11lllll_opy_(bstack1ll1l_opy_ (u"ࠩࡓ࡙࡙࠭ℑ"), bstack1llll1l11l1l_opy_, data, config)
            if not response.ok:
                raise Exception(bstack1ll1l_opy_ (u"ࠥࡗࡹࡵࡰࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡱࡳࡹࠦ࡯࡬ࠤℒ"))
        except Exception as error:
            logger.error(bstack1ll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡵࡰࠡࡤࡸ࡭ࡱࡪࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤ࡙࡫ࡳࡵࡊࡸࡦ࠿ࡀࠠࠣℓ") + str(error))
            return {
                bstack1ll1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ℔"): bstack1ll1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬℕ"),
                bstack1ll1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ№"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll1l1lll1_opy_(cls, response):
        bstack1ll1l1lll_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll1ll1111_opy_ = {}
        if bstack1ll1l1lll_opy_.get(bstack1ll1l_opy_ (u"ࠨ࡬ࡺࡸࠬ℗")) is None:
            os.environ[bstack1ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭℘")] = bstack1ll1l_opy_ (u"ࠪࡲࡺࡲ࡬ࠨℙ")
        else:
            os.environ[bstack1ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨℚ")] = bstack1ll1l1lll_opy_.get(bstack1ll1l_opy_ (u"ࠬࡰࡷࡵࠩℛ"), bstack1ll1l_opy_ (u"࠭࡮ࡶ࡮࡯ࠫℜ"))
        os.environ[bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬℝ")] = bstack1ll1l1lll_opy_.get(bstack1ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ℞"), bstack1ll1l_opy_ (u"ࠩࡱࡹࡱࡲࠧ℟"))
        logger.info(bstack1ll1l_opy_ (u"ࠪࡘࡪࡹࡴࡩࡷࡥࠤࡸࡺࡡࡳࡶࡨࡨࠥࡽࡩࡵࡪࠣ࡭ࡩࡀࠠࠨ℠") + os.getenv(bstack1ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ℡")));
        if bstack1l11llll_opy_.bstack11l11l1l1l1_opy_(cls.bs_config, cls.bstack1lll11ll1l_opy_.get(bstack1ll1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡷࡶࡩࡩ࠭™"), bstack1ll1l_opy_ (u"࠭ࠧ℣"))) is True:
            bstack11ll11ll1ll_opy_, build_hashed_id, bstack1llll11lll1l_opy_ = cls.bstack1llll1l1l1ll_opy_(bstack1ll1l1lll_opy_)
            if bstack11ll11ll1ll_opy_ != None and build_hashed_id != None:
                bstack1llll1ll1111_opy_[bstack1ll1l_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧℤ")] = {
                    bstack1ll1l_opy_ (u"ࠨ࡬ࡺࡸࡤࡺ࡯࡬ࡧࡱࠫ℥"): bstack11ll11ll1ll_opy_,
                    bstack1ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫΩ"): build_hashed_id,
                    bstack1ll1l_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧ℧"): bstack1llll11lll1l_opy_
                }
            else:
                bstack1llll1ll1111_opy_[bstack1ll1l_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫℨ")] = {}
        else:
            bstack1llll1ll1111_opy_[bstack1ll1l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ℩")] = {}
        bstack1llll1l11ll1_opy_, build_hashed_id = cls.bstack1llll1l1l11l_opy_(bstack1ll1l1lll_opy_)
        if bstack1llll1l11ll1_opy_ != None and build_hashed_id != None:
            bstack1llll1ll1111_opy_[bstack1ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭K")] = {
                bstack1ll1l_opy_ (u"ࠧࡢࡷࡷ࡬ࡤࡺ࡯࡬ࡧࡱࠫÅ"): bstack1llll1l11ll1_opy_,
                bstack1ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪℬ"): build_hashed_id,
            }
        else:
            bstack1llll1ll1111_opy_[bstack1ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩℭ")] = {}
        if bstack1llll1ll1111_opy_[bstack1ll1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ℮")].get(bstack1ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ℯ")) != None or bstack1llll1ll1111_opy_[bstack1ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬℰ")].get(bstack1ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨℱ")) != None:
            cls.bstack1llll1l1l111_opy_(bstack1ll1l1lll_opy_.get(bstack1ll1l_opy_ (u"ࠧ࡫ࡹࡷࠫℲ")), bstack1ll1l1lll_opy_.get(bstack1ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪℳ")))
        return bstack1llll1ll1111_opy_
    @classmethod
    def bstack1llll1l1l1ll_opy_(cls, bstack1ll1l1lll_opy_):
        if bstack1ll1l1lll_opy_.get(bstack1ll1l_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩℴ")) == None:
            cls.bstack1llll11lll11_opy_()
            return [None, None, None]
        if bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪℵ")][bstack1ll1l_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬℶ")] != True:
            cls.bstack1llll11lll11_opy_(bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬℷ")])
            return [None, None, None]
        logger.debug(bstack1ll1l_opy_ (u"࠭ࡻࡾࠢࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲࠡࠨℸ").format(bstack1l11l11ll1_opy_))
        os.environ[bstack1ll1l_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡇࡔࡓࡐࡍࡇࡗࡉࡉ࠭ℹ")] = bstack1ll1l_opy_ (u"ࠨࡶࡵࡹࡪ࠭℺")
        if bstack1ll1l1lll_opy_.get(bstack1ll1l_opy_ (u"ࠩ࡭ࡻࡹ࠭℻")):
            os.environ[bstack1ll1l_opy_ (u"ࠪࡇࡗࡋࡄࡆࡐࡗࡍࡆࡒࡓࡠࡈࡒࡖࡤࡉࡒࡂࡕࡋࡣࡗࡋࡐࡐࡔࡗࡍࡓࡍࠧℼ")] = json.dumps({
                bstack1ll1l_opy_ (u"ࠫࡺࡹࡥࡳࡰࡤࡱࡪ࠭ℽ"): bstack111l11l11l1_opy_(cls.bs_config),
                bstack1ll1l_opy_ (u"ࠬࡶࡡࡴࡵࡺࡳࡷࡪࠧℾ"): bstack111l11ll11l_opy_(cls.bs_config)
            })
        if bstack1ll1l1lll_opy_.get(bstack1ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨℿ")):
            os.environ[bstack1ll1l_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭⅀")] = bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ⅁")]
        if bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ⅂")].get(bstack1ll1l_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ⅃"), {}).get(bstack1ll1l_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨ⅄")):
            os.environ[bstack1ll1l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭ⅅ")] = str(bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ⅆ")][bstack1ll1l_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨⅇ")][bstack1ll1l_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬⅈ")])
        else:
            os.environ[bstack1ll1l_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪⅉ")] = bstack1ll1l_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ⅊")
        return [bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠫ࡯ࡽࡴࠨ⅋")], bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ⅌")], os.environ[bstack1ll1l_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧ⅍")]]
    @classmethod
    def bstack1llll1l1l11l_opy_(cls, bstack1ll1l1lll_opy_):
        if bstack1ll1l1lll_opy_.get(bstack1ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧⅎ")) == None:
            cls.bstack1llll1l11l11_opy_()
            return [None, None]
        if bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⅏")][bstack1ll1l_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ⅐")] != True:
            cls.bstack1llll1l11l11_opy_(bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⅑")])
            return [None, None]
        if bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⅒")].get(bstack1ll1l_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭⅓")):
            logger.debug(bstack1ll1l_opy_ (u"࠭ࡔࡦࡵࡷࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡇࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲ࡙ࠥࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠣࠪ⅔"))
            parsed = json.loads(os.getenv(bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ⅕"), bstack1ll1l_opy_ (u"ࠨࡽࢀࠫ⅖")))
            capabilities = bstack1l11lll111_opy_.bstack1llll1l11lll_opy_(bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⅗")][bstack1ll1l_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ⅘")][bstack1ll1l_opy_ (u"ࠫࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⅙")], bstack1ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ⅚"), bstack1ll1l_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬ⅛"))
            bstack1llll1l11ll1_opy_ = capabilities[bstack1ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡔࡰ࡭ࡨࡲࠬ⅜")]
            os.environ[bstack1ll1l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭⅝")] = bstack1llll1l11ll1_opy_
            if bstack1ll1l_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨࠦ⅞") in bstack1ll1l1lll_opy_ and bstack1ll1l1lll_opy_.get(bstack1ll1l_opy_ (u"ࠥࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠤ⅟")) is None:
                parsed[bstack1ll1l_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬⅠ")] = capabilities[bstack1ll1l_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭Ⅱ")]
            os.environ[bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧⅢ")] = json.dumps(parsed)
            scripts = bstack1l11lll111_opy_.bstack1llll1l11lll_opy_(bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧⅣ")][bstack1ll1l_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩⅤ")][bstack1ll1l_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪⅥ")], bstack1ll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨⅦ"), bstack1ll1l_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࠬⅧ"))
            bstack1l1ll1lll1_opy_.bstack1l11l111ll_opy_(scripts)
            commands = bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬⅨ")][bstack1ll1l_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧⅩ")][bstack1ll1l_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࡖࡲ࡛ࡷࡧࡰࠨⅪ")].get(bstack1ll1l_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪⅫ"))
            bstack1l1ll1lll1_opy_.bstack1lllll1l111l_opy_(commands)
            bstack1lllll11llll_opy_ = capabilities.get(bstack1ll1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧⅬ"))
            bstack1l1ll1lll1_opy_.bstack1lllll1l11l1_opy_(bstack1lllll11llll_opy_)
            bstack1l1ll1lll1_opy_.store()
        return [bstack1llll1l11ll1_opy_, bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬⅭ")]]
    @classmethod
    def bstack1llll11lll11_opy_(cls, response=None):
        os.environ[bstack1ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩⅮ")] = bstack1ll1l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪⅯ")
        os.environ[bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪⅰ")] = bstack1ll1l_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬⅱ")
        os.environ[bstack1ll1l_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡈࡕࡍࡑࡎࡈࡘࡊࡊࠧⅲ")] = bstack1ll1l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨⅳ")
        os.environ[bstack1ll1l_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩⅴ")] = bstack1ll1l_opy_ (u"ࠦࡳࡻ࡬࡭ࠤⅵ")
        os.environ[bstack1ll1l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭ⅶ")] = bstack1ll1l_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦⅷ")
        cls.bstack1llll1ll111l_opy_(response, bstack1ll1l_opy_ (u"ࠢࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠢⅸ"))
        return [None, None, None]
    @classmethod
    def bstack1llll1l11l11_opy_(cls, response=None):
        os.environ[bstack1ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ⅹ")] = bstack1ll1l_opy_ (u"ࠩࡱࡹࡱࡲࠧⅺ")
        os.environ[bstack1ll1l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨⅻ")] = bstack1ll1l_opy_ (u"ࠫࡳࡻ࡬࡭ࠩⅼ")
        os.environ[bstack1ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩⅽ")] = bstack1ll1l_opy_ (u"࠭࡮ࡶ࡮࡯ࠫⅾ")
        cls.bstack1llll1ll111l_opy_(response, bstack1ll1l_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠢⅿ"))
        return [None, None, None]
    @classmethod
    def bstack1llll1l1l111_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack1ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬↀ")] = jwt
        os.environ[bstack1ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧↁ")] = build_hashed_id
    @classmethod
    def bstack1llll1ll111l_opy_(cls, response=None, product=bstack1ll1l_opy_ (u"ࠥࠦↂ")):
        if response == None or response.get(bstack1ll1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࡶࠫↃ")) == None:
            logger.error(product + bstack1ll1l_opy_ (u"ࠧࠦࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠢↄ"))
            return
        for error in response[bstack1ll1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭ↅ")]:
            bstack111l11l1l11_opy_ = error[bstack1ll1l_opy_ (u"ࠧ࡬ࡧࡼࠫↆ")]
            error_message = error[bstack1ll1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩↇ")]
            if error_message:
                if bstack111l11l1l11_opy_ == bstack1ll1l_opy_ (u"ࠤࡈࡖࡗࡕࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡆࡈࡒࡎࡋࡄࠣↈ"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack1ll1l_opy_ (u"ࠥࡈࡦࡺࡡࠡࡷࡳࡰࡴࡧࡤࠡࡶࡲࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࠦ↉") + product + bstack1ll1l_opy_ (u"ࠦࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡪࡵࡦࠢࡷࡳࠥࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠤ↊"))
    @classmethod
    def bstack1llll11llll1_opy_(cls):
        if cls.bstack11l11l1lll1_opy_ is not None:
            return
        cls.bstack11l11l1lll1_opy_ = bstack111ll111ll1_opy_(cls.post_data)
        cls.bstack11l11l1lll1_opy_.start()
    @classmethod
    def bstack1l111l1l_opy_(cls):
        if cls.bstack11l11l1lll1_opy_ is None:
            return
        cls.bstack11l11l1lll1_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1lll111l_opy_, event_url=bstack1ll1l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡡࡵࡥ࡫ࠫ↋")):
        config = {
            bstack1ll1l_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ↌"): cls.default_headers()
        }
        logger.debug(bstack1ll1l_opy_ (u"ࠢࡱࡱࡶࡸࡤࡪࡡࡵࡣ࠽ࠤࡘ࡫࡮ࡥ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡸࡴࠦࡴࡦࡵࡷ࡬ࡺࡨࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶࡶࠤࢀࢃࠢ↍").format(bstack1ll1l_opy_ (u"ࠨ࠮ࠣࠫ↎").join([event[bstack1ll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭↏")] for event in bstack1lll111l_opy_])))
        response = bstack1l11lllll_opy_(bstack1ll1l_opy_ (u"ࠪࡔࡔ࡙ࡔࠨ←"), cls.request_url(event_url), bstack1lll111l_opy_, config)
        bstack1lllll111111_opy_ = response.json()
    @classmethod
    def bstack1ll11l11_opy_(cls, bstack1lll111l_opy_, event_url=bstack1ll1l_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪ↑")):
        logger.debug(bstack1ll1l_opy_ (u"ࠧࡹࡥ࡯ࡦࡢࡨࡦࡺࡡ࠻ࠢࡄࡸࡹ࡫࡭ࡱࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡤࡨࡩࠦࡤࡢࡶࡤࠤࡹࡵࠠࡣࡣࡷࡧ࡭ࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥ࠻ࠢࡾࢁࠧ→").format(bstack1lll111l_opy_[bstack1ll1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ↓")]))
        if not bstack1l11lll111_opy_.bstack1llll1l111ll_opy_(bstack1lll111l_opy_[bstack1ll1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ↔")]):
            logger.debug(bstack1ll1l_opy_ (u"ࠣࡵࡨࡲࡩࡥࡤࡢࡶࡤ࠾ࠥࡔ࡯ࡵࠢࡤࡨࡩ࡯࡮ࡨࠢࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨ↕").format(bstack1lll111l_opy_[bstack1ll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭↖")]))
            return
        bstack11ll1ll11l_opy_ = bstack1l11lll111_opy_.bstack1llll11ll1l1_opy_(bstack1lll111l_opy_[bstack1ll1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ↗")], bstack1lll111l_opy_.get(bstack1ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭↘")))
        if bstack11ll1ll11l_opy_ != None:
            if bstack1lll111l_opy_.get(bstack1ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧ↙")) != None:
                bstack1lll111l_opy_[bstack1ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨ↚")][bstack1ll1l_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ↛")] = bstack11ll1ll11l_opy_
            else:
                bstack1lll111l_opy_[bstack1ll1l_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭↜")] = bstack11ll1ll11l_opy_
        if event_url == bstack1ll1l_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨ↝"):
            cls.bstack1llll11llll1_opy_()
            logger.debug(bstack1ll1l_opy_ (u"ࠥࡷࡪࡴࡤࡠࡦࡤࡸࡦࡀࠠࡂࡦࡧ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥࡺ࡯ࠡࡤࡤࡸࡨ࡮ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨ↞").format(bstack1lll111l_opy_[bstack1ll1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ↟")]))
            cls.bstack11l11l1lll1_opy_.add(bstack1lll111l_opy_)
        elif event_url == bstack1ll1l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪ↠"):
            cls.post_data([bstack1lll111l_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1l1lll1l_opy_(cls, logs):
        for log in logs:
            bstack1llll1l1ll11_opy_ = {
                bstack1ll1l_opy_ (u"࠭࡫ࡪࡰࡧࠫ↡"): bstack1ll1l_opy_ (u"ࠧࡕࡇࡖࡘࡤࡒࡏࡈࠩ↢"),
                bstack1ll1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ↣"): log[bstack1ll1l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ↤")],
                bstack1ll1l_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭↥"): log[bstack1ll1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ↦")],
                bstack1ll1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡢࡶࡪࡹࡰࡰࡰࡶࡩࠬ↧"): {},
                bstack1ll1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ↨"): log[bstack1ll1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ↩")],
            }
            if bstack1ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ↪") in log:
                bstack1llll1l1ll11_opy_[bstack1ll1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ↫")] = log[bstack1ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ↬")]
            elif bstack1ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ↭") in log:
                bstack1llll1l1ll11_opy_[bstack1ll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ↮")] = log[bstack1ll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭↯")]
            cls.bstack1ll11l11_opy_({
                bstack1ll1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ↰"): bstack1ll1l_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬ↱"),
                bstack1ll1l_opy_ (u"ࠩ࡯ࡳ࡬ࡹࠧ↲"): [bstack1llll1l1ll11_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll1l1ll1l_opy_(cls, steps):
        bstack1llll1l111l1_opy_ = []
        for step in steps:
            bstack1llll11lllll_opy_ = {
                bstack1ll1l_opy_ (u"ࠪ࡯࡮ࡴࡤࠨ↳"): bstack1ll1l_opy_ (u"࡙ࠫࡋࡓࡕࡡࡖࡘࡊࡖࠧ↴"),
                bstack1ll1l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ↵"): step[bstack1ll1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ↶")],
                bstack1ll1l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ↷"): step[bstack1ll1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ↸")],
                bstack1ll1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ↹"): step[bstack1ll1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ↺")],
                bstack1ll1l_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭↻"): step[bstack1ll1l_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧ↼")]
            }
            if bstack1ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭↽") in step:
                bstack1llll11lllll_opy_[bstack1ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ↾")] = step[bstack1ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ↿")]
            elif bstack1ll1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇀") in step:
                bstack1llll11lllll_opy_[bstack1ll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇁")] = step[bstack1ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇂")]
            bstack1llll1l111l1_opy_.append(bstack1llll11lllll_opy_)
        cls.bstack1ll11l11_opy_({
            bstack1ll1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ⇃"): bstack1ll1l_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ⇄"),
            bstack1ll1l_opy_ (u"ࠧ࡭ࡱࡪࡷࠬ⇅"): bstack1llll1l111l1_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l1l1ll11_opy_, stage=STAGE.bstack11lll11ll_opy_)
    def bstack1l1l1l1lll_opy_(cls, screenshot):
        cls.bstack1ll11l11_opy_({
            bstack1ll1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ⇆"): bstack1ll1l_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭⇇"),
            bstack1ll1l_opy_ (u"ࠪࡰࡴ࡭ࡳࠨ⇈"): [{
                bstack1ll1l_opy_ (u"ࠫࡰ࡯࡮ࡥࠩ⇉"): bstack1ll1l_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࠧ⇊"),
                bstack1ll1l_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ⇋"): datetime.datetime.utcnow().isoformat() + bstack1ll1l_opy_ (u"࡛ࠧࠩ⇌"),
                bstack1ll1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⇍"): screenshot[bstack1ll1l_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨ⇎")],
                bstack1ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇏"): screenshot[bstack1ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇐")]
            }]
        }, event_url=bstack1ll1l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪ⇑"))
    @classmethod
    @error_handler(class_method=True)
    def bstack111ll1lll1_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1ll11l11_opy_({
            bstack1ll1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⇒"): bstack1ll1l_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫ⇓"),
            bstack1ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪ⇔"): {
                bstack1ll1l_opy_ (u"ࠤࡸࡹ࡮ࡪࠢ⇕"): cls.current_test_uuid(),
                bstack1ll1l_opy_ (u"ࠥ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠤ⇖"): cls.bstack1llll111_opy_(driver)
            }
        })
    @classmethod
    def bstack11lll1l1_opy_(cls, event: str, bstack1lll111l_opy_: bstack1ll1llll_opy_):
        bstack1ll1l1ll_opy_ = {
            bstack1ll1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⇗"): event,
            bstack1lll111l_opy_.event_key(): bstack1lll111l_opy_.bstack1llll1ll_opy_(event)
        }
        cls.bstack1ll11l11_opy_(bstack1ll1l1ll_opy_)
        result = getattr(bstack1lll111l_opy_, bstack1ll1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⇘"), None)
        if event == bstack1ll1l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ⇙"):
            threading.current_thread().bstackTestMeta = {bstack1ll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ⇚"): bstack1ll1l_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩ⇛")}
        elif event == bstack1ll1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ⇜"):
            threading.current_thread().bstackTestMeta = {bstack1ll1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ⇝"): getattr(result, bstack1ll1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ⇞"), bstack1ll1l_opy_ (u"ࠬ࠭⇟"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ⇠"), None) is None or os.environ[bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ⇡")] == bstack1ll1l_opy_ (u"ࠣࡰࡸࡰࡱࠨ⇢")) and (os.environ.get(bstack1ll1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ⇣"), None) is None or os.environ[bstack1ll1l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ⇤")] == bstack1ll1l_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ⇥")):
            return False
        return True
    @staticmethod
    def bstack1llll1l11111_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1lllll11_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack1ll1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ⇦"): bstack1ll1l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ⇧"),
            bstack1ll1l_opy_ (u"࡙ࠧ࠯ࡅࡗ࡙ࡇࡃࡌ࠯ࡗࡉࡘ࡚ࡏࡑࡕࠪ⇨"): bstack1ll1l_opy_ (u"ࠨࡶࡵࡹࡪ࠭⇩")
        }
        if os.environ.get(bstack1ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭⇪"), None):
            headers[bstack1ll1l_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪ⇫")] = bstack1ll1l_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧ⇬").format(os.environ[bstack1ll1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠤ⇭")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack1ll1l_opy_ (u"࠭ࡻࡾ࠱ࡾࢁࠬ⇮").format(bstack1llll1l1l1l1_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack1ll1l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ⇯"), None)
    @staticmethod
    def bstack1llll111_opy_(driver):
        return {
            bstack1111lllllll_opy_(): bstack111l11ll1ll_opy_(driver)
        }
    @staticmethod
    def bstack1llll11ll1ll_opy_(exception_info, report):
        return [{bstack1ll1l_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫ⇰"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11111l11l1_opy_(typename):
        if bstack1ll1l_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧ⇱") in typename:
            return bstack1ll1l_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦ⇲")
        return bstack1ll1l_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧ⇳")