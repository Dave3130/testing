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
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111l11lll1l_opy_, bstack111l11ll111_opy_, bstack11lll1llll_opy_, error_handler, bstack111l111l1ll_opy_, bstack1111ll111l1_opy_, bstack1111lll1l11_opy_, bstack1ll1ll11_opy_, bstack11lll111_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l11l1l1ll_opy_ import bstack111ll11l1l1_opy_
import bstack_utils.bstack1111lll1ll_opy_ as bstack1l11l1l11l_opy_
from bstack_utils.bstack11llllll_opy_ import bstack1ll1l1ll_opy_
import bstack_utils.accessibility as bstack111l1lll_opy_
from bstack_utils.bstack11l1ll11ll_opy_ import bstack11l1ll11ll_opy_
from bstack_utils.bstack1l11lll1_opy_ import bstack1lll1l11_opy_
from bstack_utils.constants import bstack11l1111l1l_opy_
bstack1llll1l1111l_opy_ = bstack11l1l11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡧࡴࡲ࡬ࡦࡥࡷࡳࡷ࠳࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩ⃵")
logger = logging.getLogger(__name__)
class bstack1l1lll1l_opy_:
    bstack11l11l1l1ll_opy_ = None
    bs_config = None
    bstack11l1l1l11_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l1l11l1ll_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def launch(cls, bs_config, bstack11l1l1l11_opy_):
        cls.bs_config = bs_config
        cls.bstack11l1l1l11_opy_ = bstack11l1l1l11_opy_
        try:
            cls.bstack1llll1l1lll1_opy_()
            bstack1lllll111lll_opy_ = bstack111l11lll1l_opy_(bs_config)
            bstack1llll1ll11ll_opy_ = bstack111l11ll111_opy_(bs_config)
            data = bstack1l11l1l11l_opy_.bstack1llll1l11111_opy_(bs_config, bstack11l1l1l11_opy_)
            config = {
                bstack11l1l11_opy_ (u"ࠪࡥࡺࡺࡨࠨ⃶"): (bstack1lllll111lll_opy_, bstack1llll1ll11ll_opy_),
                bstack11l1l11_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ⃷"): cls.default_headers()
            }
            response = bstack11lll1llll_opy_(bstack11l1l11_opy_ (u"ࠬࡖࡏࡔࡖࠪ⃸"), cls.request_url(bstack11l1l11_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠷࠵ࡢࡶ࡫࡯ࡨࡸ࠭⃹")), data, config)
            if response.status_code != 200:
                bstack1ll11l11l1_opy_ = response.json()
                if bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨ⃺")] == False:
                    cls.bstack1llll1l111l1_opy_(bstack1ll11l11l1_opy_)
                    return
                cls.bstack1llll1l111ll_opy_(bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ⃻")])
                cls.bstack1llll1l11l1l_opy_(bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⃼")])
                return None
            bstack1llll1l11lll_opy_ = cls.bstack1llll11lll1l_opy_(response)
            return bstack1llll1l11lll_opy_, response.json()
        except Exception as error:
            logger.error(bstack11l1l11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࠦࡦࡰࡴࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࢁࡽࠣ⃽").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll1l11l11_opy_=None):
        if not bstack1ll1l1ll_opy_.on() and not bstack111l1lll_opy_.on():
            return
        if os.environ.get(bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ⃾")) == bstack11l1l11_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ⃿") or os.environ.get(bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ℀")) == bstack11l1l11_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ℁"):
            logger.error(bstack11l1l11_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡶࡲࡴࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡺ࡯ࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࡑ࡮ࡹࡳࡪࡰࡪࠤࡦࡻࡴࡩࡧࡱࡸ࡮ࡩࡡࡵ࡫ࡲࡲࠥࡺ࡯࡬ࡧࡱࠫℂ"))
            return {
                bstack11l1l11_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ℃"): bstack11l1l11_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ℄"),
                bstack11l1l11_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ℅"): bstack11l1l11_opy_ (u"࡚ࠬ࡯࡬ࡧࡱ࠳ࡧࡻࡩ࡭ࡦࡌࡈࠥ࡯ࡳࠡࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧ࠰ࠥࡨࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦ࡭ࡪࡩ࡫ࡸࠥ࡮ࡡࡷࡧࠣࡪࡦ࡯࡬ࡦࡦࠪ℆")
            }
        try:
            cls.bstack11l11l1l1ll_opy_.shutdown()
            data = {
                bstack11l1l11_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫℇ"): bstack1ll1ll11_opy_()
            }
            if not bstack1llll1l11l11_opy_ is None:
                data[bstack11l1l11_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡰࡩࡹࡧࡤࡢࡶࡤࠫ℈")] = [{
                    bstack11l1l11_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨ℉"): bstack11l1l11_opy_ (u"ࠩࡸࡷࡪࡸ࡟࡬࡫࡯ࡰࡪࡪࠧℊ"),
                    bstack11l1l11_opy_ (u"ࠪࡷ࡮࡭࡮ࡢ࡮ࠪℋ"): bstack1llll1l11l11_opy_
                }]
            config = {
                bstack11l1l11_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬℌ"): cls.default_headers()
            }
            bstack11ll11l1ll1_opy_ = bstack11l1l11_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽ࠰ࡵࡷࡳࡵ࠭ℍ").format(os.environ[bstack11l1l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦℎ")])
            bstack1llll1l1l111_opy_ = cls.request_url(bstack11ll11l1ll1_opy_)
            response = bstack11lll1llll_opy_(bstack11l1l11_opy_ (u"ࠧࡑࡗࡗࠫℏ"), bstack1llll1l1l111_opy_, data, config)
            if not response.ok:
                raise Exception(bstack11l1l11_opy_ (u"ࠣࡕࡷࡳࡵࠦࡲࡦࡳࡸࡩࡸࡺࠠ࡯ࡱࡷࠤࡴࡱࠢℐ"))
        except Exception as error:
            logger.error(bstack11l1l11_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡷࡳࡵࠦࡢࡶ࡫࡯ࡨࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡗࡩࡸࡺࡈࡶࡤ࠽࠾ࠥࠨℑ") + str(error))
            return {
                bstack11l1l11_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪℒ"): bstack11l1l11_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪℓ"),
                bstack11l1l11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭℔"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11lll1l_opy_(cls, response):
        bstack1ll11l11l1_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll1l11lll_opy_ = {}
        if bstack1ll11l11l1_opy_.get(bstack11l1l11_opy_ (u"࠭ࡪࡸࡶࠪℕ")) is None:
            os.environ[bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ№")] = bstack11l1l11_opy_ (u"ࠨࡰࡸࡰࡱ࠭℗")
        else:
            os.environ[bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭℘")] = bstack1ll11l11l1_opy_.get(bstack11l1l11_opy_ (u"ࠪ࡮ࡼࡺࠧℙ"), bstack11l1l11_opy_ (u"ࠫࡳࡻ࡬࡭ࠩℚ"))
        os.environ[bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪℛ")] = bstack1ll11l11l1_opy_.get(bstack11l1l11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨℜ"), bstack11l1l11_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬℝ"))
        logger.info(bstack11l1l11_opy_ (u"ࠨࡖࡨࡷࡹ࡮ࡵࡣࠢࡶࡸࡦࡸࡴࡦࡦࠣࡻ࡮ࡺࡨࠡ࡫ࡧ࠾ࠥ࠭℞") + os.getenv(bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ℟")));
        if bstack1ll1l1ll_opy_.bstack11l11l1ll1l_opy_(cls.bs_config, cls.bstack11l1l1l11_opy_.get(bstack11l1l11_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡵࡴࡧࡧࠫ℠"), bstack11l1l11_opy_ (u"ࠫࠬ℡"))) is True:
            bstack11ll11ll1l1_opy_, build_hashed_id, bstack1llll1l1l1ll_opy_ = cls.bstack1llll1l11ll1_opy_(bstack1ll11l11l1_opy_)
            if bstack11ll11ll1l1_opy_ != None and build_hashed_id != None:
                bstack1llll1l11lll_opy_[bstack11l1l11_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ™")] = {
                    bstack11l1l11_opy_ (u"࠭ࡪࡸࡶࡢࡸࡴࡱࡥ࡯ࠩ℣"): bstack11ll11ll1l1_opy_,
                    bstack11l1l11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩℤ"): build_hashed_id,
                    bstack11l1l11_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬ℥"): bstack1llll1l1l1ll_opy_
                }
            else:
                bstack1llll1l11lll_opy_[bstack11l1l11_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩΩ")] = {}
        else:
            bstack1llll1l11lll_opy_[bstack11l1l11_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ℧")] = {}
        bstack1llll1l1ll1l_opy_, build_hashed_id = cls.bstack1llll1l1llll_opy_(bstack1ll11l11l1_opy_)
        if bstack1llll1l1ll1l_opy_ != None and build_hashed_id != None:
            bstack1llll1l11lll_opy_[bstack11l1l11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫℨ")] = {
                bstack11l1l11_opy_ (u"ࠬࡧࡵࡵࡪࡢࡸࡴࡱࡥ࡯ࠩ℩"): bstack1llll1l1ll1l_opy_,
                bstack11l1l11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨK"): build_hashed_id,
            }
        else:
            bstack1llll1l11lll_opy_[bstack11l1l11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧÅ")] = {}
        if bstack1llll1l11lll_opy_[bstack11l1l11_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨℬ")].get(bstack11l1l11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫℭ")) != None or bstack1llll1l11lll_opy_[bstack11l1l11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ℮")].get(bstack11l1l11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ℯ")) != None:
            cls.bstack1llll1l1l11l_opy_(bstack1ll11l11l1_opy_.get(bstack11l1l11_opy_ (u"ࠬࡰࡷࡵࠩℰ")), bstack1ll11l11l1_opy_.get(bstack11l1l11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨℱ")))
        return bstack1llll1l11lll_opy_
    @classmethod
    def bstack1llll1l11ll1_opy_(cls, bstack1ll11l11l1_opy_):
        if bstack1ll11l11l1_opy_.get(bstack11l1l11_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧℲ")) == None:
            cls.bstack1llll1l111ll_opy_()
            return [None, None, None]
        if bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨℳ")][bstack11l1l11_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪℴ")] != True:
            cls.bstack1llll1l111ll_opy_(bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪℵ")])
            return [None, None, None]
        logger.debug(bstack11l1l11_opy_ (u"ࠫࢀࢃࠠࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࠦ࠭ℶ").format(bstack11l1111l1l_opy_))
        os.environ[bstack11l1l11_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡅࡒࡑࡕࡒࡅࡕࡇࡇࠫℷ")] = bstack11l1l11_opy_ (u"࠭ࡴࡳࡷࡨࠫℸ")
        if bstack1ll11l11l1_opy_.get(bstack11l1l11_opy_ (u"ࠧ࡫ࡹࡷࠫℹ")):
            os.environ[bstack11l1l11_opy_ (u"ࠨࡅࡕࡉࡉࡋࡎࡕࡋࡄࡐࡘࡥࡆࡐࡔࡢࡇࡗࡇࡓࡉࡡࡕࡉࡕࡕࡒࡕࡋࡑࡋࠬ℺")] = json.dumps({
                bstack11l1l11_opy_ (u"ࠩࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫ℻"): bstack111l11lll1l_opy_(cls.bs_config),
                bstack11l1l11_opy_ (u"ࠪࡴࡦࡹࡳࡸࡱࡵࡨࠬℼ"): bstack111l11ll111_opy_(cls.bs_config)
            })
        if bstack1ll11l11l1_opy_.get(bstack11l1l11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ℽ")):
            os.environ[bstack11l1l11_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡊࡄࡗࡍࡋࡄࡠࡋࡇࠫℾ")] = bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨℿ")]
        if bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ⅀")].get(bstack11l1l11_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩ⅁"), {}).get(bstack11l1l11_opy_ (u"ࠩࡤࡰࡱࡵࡷࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭⅂")):
            os.environ[bstack11l1l11_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫ⅃")] = str(bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ⅄")][bstack11l1l11_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭ⅅ")][bstack11l1l11_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪⅆ")])
        else:
            os.environ[bstack11l1l11_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡆࡒࡌࡐ࡙ࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࡓࠨⅇ")] = bstack11l1l11_opy_ (u"ࠣࡰࡸࡰࡱࠨⅈ")
        return [bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠩ࡭ࡻࡹ࠭ⅉ")], bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ⅊")], os.environ[bstack11l1l11_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡃࡏࡐࡔ࡝࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࡗࠬ⅋")]]
    @classmethod
    def bstack1llll1l1llll_opy_(cls, bstack1ll11l11l1_opy_):
        if bstack1ll11l11l1_opy_.get(bstack11l1l11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⅌")) == None:
            cls.bstack1llll1l11l1l_opy_()
            return [None, None]
        if bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⅍")][bstack11l1l11_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨⅎ")] != True:
            cls.bstack1llll1l11l1l_opy_(bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⅏")])
            return [None, None]
        if bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⅐")].get(bstack11l1l11_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ⅑")):
            logger.debug(bstack11l1l11_opy_ (u"࡙ࠫ࡫ࡳࡵࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲࠡࠨ⅒"))
            parsed = json.loads(os.getenv(bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭⅓"), bstack11l1l11_opy_ (u"࠭ࡻࡾࠩ⅔")))
            capabilities = bstack1l11l1l11l_opy_.bstack1llll11lll11_opy_(bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⅕")][bstack11l1l11_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩ⅖")][bstack11l1l11_opy_ (u"ࠩࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⅗")], bstack11l1l11_opy_ (u"ࠪࡲࡦࡳࡥࠨ⅘"), bstack11l1l11_opy_ (u"ࠫࡻࡧ࡬ࡶࡧࠪ⅙"))
            bstack1llll1l1ll1l_opy_ = capabilities[bstack11l1l11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࡙ࡵ࡫ࡦࡰࠪ⅚")]
            os.environ[bstack11l1l11_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ⅛")] = bstack1llll1l1ll1l_opy_
            if bstack11l1l11_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡦࠤ⅜") in bstack1ll11l11l1_opy_ and bstack1ll11l11l1_opy_.get(bstack11l1l11_opy_ (u"ࠣࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠢ⅝")) is None:
                parsed[bstack11l1l11_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ⅞")] = capabilities[bstack11l1l11_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ⅟")]
            os.environ[bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬⅠ")] = json.dumps(parsed)
            scripts = bstack1l11l1l11l_opy_.bstack1llll11lll11_opy_(bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬⅡ")][bstack11l1l11_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧⅢ")][bstack11l1l11_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨⅣ")], bstack11l1l11_opy_ (u"ࠨࡰࡤࡱࡪ࠭Ⅴ"), bstack11l1l11_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࠪⅥ"))
            bstack11l1ll11ll_opy_.bstack1ll11ll11l_opy_(scripts)
            commands = bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪⅦ")][bstack11l1l11_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬⅧ")][bstack11l1l11_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࡔࡰ࡙ࡵࡥࡵ࠭Ⅸ")].get(bstack11l1l11_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨⅩ"))
            bstack11l1ll11ll_opy_.bstack1lllll1l1111_opy_(commands)
            bstack1lllll1l11ll_opy_ = capabilities.get(bstack11l1l11_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬⅪ"))
            bstack11l1ll11ll_opy_.bstack1lllll11llll_opy_(bstack1lllll1l11ll_opy_)
            bstack11l1ll11ll_opy_.store()
        return [bstack1llll1l1ll1l_opy_, bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪⅫ")]]
    @classmethod
    def bstack1llll1l111ll_opy_(cls, response=None):
        os.environ[bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧⅬ")] = bstack11l1l11_opy_ (u"ࠪࡲࡺࡲ࡬ࠨⅭ")
        os.environ[bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨⅮ")] = bstack11l1l11_opy_ (u"ࠬࡴࡵ࡭࡮ࠪⅯ")
        os.environ[bstack11l1l11_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡆࡓࡒࡖࡌࡆࡖࡈࡈࠬⅰ")] = bstack11l1l11_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ⅱ")
        os.environ[bstack11l1l11_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧⅲ")] = bstack11l1l11_opy_ (u"ࠤࡱࡹࡱࡲࠢⅳ")
        os.environ[bstack11l1l11_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫⅴ")] = bstack11l1l11_opy_ (u"ࠦࡳࡻ࡬࡭ࠤⅵ")
        cls.bstack1llll1l111l1_opy_(response, bstack11l1l11_opy_ (u"ࠧࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠧⅶ"))
        return [None, None, None]
    @classmethod
    def bstack1llll1l11l1l_opy_(cls, response=None):
        os.environ[bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫⅷ")] = bstack11l1l11_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬⅸ")
        os.environ[bstack11l1l11_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ⅹ")] = bstack11l1l11_opy_ (u"ࠩࡱࡹࡱࡲࠧⅺ")
        os.environ[bstack11l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧⅻ")] = bstack11l1l11_opy_ (u"ࠫࡳࡻ࡬࡭ࠩⅼ")
        cls.bstack1llll1l111l1_opy_(response, bstack11l1l11_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠧⅽ"))
        return [None, None, None]
    @classmethod
    def bstack1llll1l1l11l_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪⅾ")] = jwt
        os.environ[bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬⅿ")] = build_hashed_id
    @classmethod
    def bstack1llll1l111l1_opy_(cls, response=None, product=bstack11l1l11_opy_ (u"ࠣࠤↀ")):
        if response == None or response.get(bstack11l1l11_opy_ (u"ࠩࡨࡶࡷࡵࡲࡴࠩↁ")) == None:
            logger.error(product + bstack11l1l11_opy_ (u"ࠥࠤࡇࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠧↂ"))
            return
        for error in response[bstack11l1l11_opy_ (u"ࠫࡪࡸࡲࡰࡴࡶࠫↃ")]:
            bstack111l1l111ll_opy_ = error[bstack11l1l11_opy_ (u"ࠬࡱࡥࡺࠩↄ")]
            error_message = error[bstack11l1l11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧↅ")]
            if error_message:
                if bstack111l1l111ll_opy_ == bstack11l1l11_opy_ (u"ࠢࡆࡔࡕࡓࡗࡥࡁࡄࡅࡈࡗࡘࡥࡄࡆࡐࡌࡉࡉࠨↆ"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack11l1l11_opy_ (u"ࠣࡆࡤࡸࡦࠦࡵࡱ࡮ࡲࡥࡩࠦࡴࡰࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࠤↇ") + product + bstack11l1l11_opy_ (u"ࠤࠣࡪࡦ࡯࡬ࡦࡦࠣࡨࡺ࡫ࠠࡵࡱࠣࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠢↈ"))
    @classmethod
    def bstack1llll1l1lll1_opy_(cls):
        if cls.bstack11l11l1l1ll_opy_ is not None:
            return
        cls.bstack11l11l1l1ll_opy_ = bstack111ll11l1l1_opy_(cls.post_data)
        cls.bstack11l11l1l1ll_opy_.start()
    @classmethod
    def bstack1ll11lll_opy_(cls):
        if cls.bstack11l11l1l1ll_opy_ is None:
            return
        cls.bstack11l11l1l1ll_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1l11ll1l_opy_, event_url=bstack11l1l11_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡦࡺࡣࡩࠩ↉")):
        config = {
            bstack11l1l11_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ↊"): cls.default_headers()
        }
        logger.debug(bstack11l1l11_opy_ (u"ࠧࡶ࡯ࡴࡶࡢࡨࡦࡺࡡ࠻ࠢࡖࡩࡳࡪࡩ࡯ࡩࠣࡨࡦࡺࡡࠡࡶࡲࠤࡹ࡫ࡳࡵࡪࡸࡦࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴࡴࠢࡾࢁࠧ↋").format(bstack11l1l11_opy_ (u"࠭ࠬࠡࠩ↌").join([event[bstack11l1l11_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ↍")] for event in bstack1l11ll1l_opy_])))
        response = bstack11lll1llll_opy_(bstack11l1l11_opy_ (u"ࠨࡒࡒࡗ࡙࠭↎"), cls.request_url(event_url), bstack1l11ll1l_opy_, config)
        bstack1llll1llllll_opy_ = response.json()
    @classmethod
    def bstack1l1lll11_opy_(cls, bstack1l11ll1l_opy_, event_url=bstack11l1l11_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨ↏")):
        logger.debug(bstack11l1l11_opy_ (u"ࠥࡷࡪࡴࡤࡠࡦࡤࡸࡦࡀࠠࡂࡶࡷࡩࡲࡶࡴࡪࡰࡪࠤࡹࡵࠠࡢࡦࡧࠤࡩࡧࡴࡢࠢࡷࡳࠥࡨࡡࡵࡥ࡫ࠤࡼ࡯ࡴࡩࠢࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪࡀࠠࡼࡿࠥ←").format(bstack1l11ll1l_opy_[bstack11l1l11_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ↑")]))
        if not bstack1l11l1l11l_opy_.bstack1llll11llll1_opy_(bstack1l11ll1l_opy_[bstack11l1l11_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ→")]):
            logger.debug(bstack11l1l11_opy_ (u"ࠨࡳࡦࡰࡧࡣࡩࡧࡴࡢ࠼ࠣࡒࡴࡺࠠࡢࡦࡧ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫࠺ࠡࡽࢀࠦ↓").format(bstack1l11ll1l_opy_[bstack11l1l11_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ↔")]))
            return
        bstack1l1l111111_opy_ = bstack1l11l1l11l_opy_.bstack1llll1ll1111_opy_(bstack1l11ll1l_opy_[bstack11l1l11_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ↕")], bstack1l11ll1l_opy_.get(bstack11l1l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ↖")))
        if bstack1l1l111111_opy_ != None:
            if bstack1l11ll1l_opy_.get(bstack11l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬ↗")) != None:
                bstack1l11ll1l_opy_[bstack11l1l11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭↘")][bstack11l1l11_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪ↙")] = bstack1l1l111111_opy_
            else:
                bstack1l11ll1l_opy_[bstack11l1l11_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫ↚")] = bstack1l1l111111_opy_
        if event_url == bstack11l1l11_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡣࡷࡧ࡭࠭↛"):
            cls.bstack1llll1l1lll1_opy_()
            logger.debug(bstack11l1l11_opy_ (u"ࠣࡵࡨࡲࡩࡥࡤࡢࡶࡤ࠾ࠥࡇࡤࡥ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡸࡴࠦࡢࡢࡶࡦ࡬ࠥࡽࡩࡵࡪࠣࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫࠺ࠡࡽࢀࠦ↜").format(bstack1l11ll1l_opy_[bstack11l1l11_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭↝")]))
            cls.bstack11l11l1l1ll_opy_.add(bstack1l11ll1l_opy_)
        elif event_url == bstack11l1l11_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨ↞"):
            cls.post_data([bstack1l11ll1l_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1l1l1111_opy_(cls, logs):
        for log in logs:
            bstack1llll11ll1l1_opy_ = {
                bstack11l1l11_opy_ (u"ࠫࡰ࡯࡮ࡥࠩ↟"): bstack11l1l11_opy_ (u"࡚ࠬࡅࡔࡖࡢࡐࡔࡍࠧ↠"),
                bstack11l1l11_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ↡"): log[bstack11l1l11_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭↢")],
                bstack11l1l11_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ↣"): log[bstack11l1l11_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ↤")],
                bstack11l1l11_opy_ (u"ࠪ࡬ࡹࡺࡰࡠࡴࡨࡷࡵࡵ࡮ࡴࡧࠪ↥"): {},
                bstack11l1l11_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ↦"): log[bstack11l1l11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭↧")],
            }
            if bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭↨") in log:
                bstack1llll11ll1l1_opy_[bstack11l1l11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ↩")] = log[bstack11l1l11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ↪")]
            elif bstack11l1l11_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ↫") in log:
                bstack1llll11ll1l1_opy_[bstack11l1l11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ↬")] = log[bstack11l1l11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ↭")]
            cls.bstack1l1lll11_opy_({
                bstack11l1l11_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ↮"): bstack11l1l11_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ↯"),
                bstack11l1l11_opy_ (u"ࠧ࡭ࡱࡪࡷࠬ↰"): [bstack1llll11ll1l1_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11lllll_opy_(cls, steps):
        bstack1llll1l1l1l1_opy_ = []
        for step in steps:
            bstack1llll1ll111l_opy_ = {
                bstack11l1l11_opy_ (u"ࠨ࡭࡬ࡲࡩ࠭↱"): bstack11l1l11_opy_ (u"ࠩࡗࡉࡘ࡚࡟ࡔࡖࡈࡔࠬ↲"),
                bstack11l1l11_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ↳"): step[bstack11l1l11_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ↴")],
                bstack11l1l11_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ↵"): step[bstack11l1l11_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ↶")],
                bstack11l1l11_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ↷"): step[bstack11l1l11_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ↸")],
                bstack11l1l11_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫ↹"): step[bstack11l1l11_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬ↺")]
            }
            if bstack11l1l11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ↻") in step:
                bstack1llll1ll111l_opy_[bstack11l1l11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ↼")] = step[bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭↽")]
            elif bstack11l1l11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ↾") in step:
                bstack1llll1ll111l_opy_[bstack11l1l11_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ↿")] = step[bstack11l1l11_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇀")]
            bstack1llll1l1l1l1_opy_.append(bstack1llll1ll111l_opy_)
        cls.bstack1l1lll11_opy_({
            bstack11l1l11_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ⇁"): bstack11l1l11_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨ⇂"),
            bstack11l1l11_opy_ (u"ࠬࡲ࡯ࡨࡵࠪ⇃"): bstack1llll1l1l1l1_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack1lll1l1lll_opy_, stage=STAGE.bstack11l1lllll_opy_)
    def bstack1l11l1lll_opy_(cls, screenshot):
        cls.bstack1l1lll11_opy_({
            bstack11l1l11_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⇄"): bstack11l1l11_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫ⇅"),
            bstack11l1l11_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭⇆"): [{
                bstack11l1l11_opy_ (u"ࠩ࡮࡭ࡳࡪࠧ⇇"): bstack11l1l11_opy_ (u"ࠪࡘࡊ࡙ࡔࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࠬ⇈"),
                bstack11l1l11_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ⇉"): datetime.datetime.utcnow().isoformat() + bstack11l1l11_opy_ (u"ࠬࡠࠧ⇊"),
                bstack11l1l11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⇋"): screenshot[bstack11l1l11_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭⇌")],
                bstack11l1l11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇍"): screenshot[bstack11l1l11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇎")]
            }]
        }, event_url=bstack11l1l11_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨ⇏"))
    @classmethod
    @error_handler(class_method=True)
    def bstack111ll11ll1_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1l1lll11_opy_({
            bstack11l1l11_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⇐"): bstack11l1l11_opy_ (u"ࠬࡉࡂࡕࡕࡨࡷࡸ࡯࡯࡯ࡅࡵࡩࡦࡺࡥࡥࠩ⇑"),
            bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨ⇒"): {
                bstack11l1l11_opy_ (u"ࠢࡶࡷ࡬ࡨࠧ⇓"): cls.current_test_uuid(),
                bstack11l1l11_opy_ (u"ࠣ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠢ⇔"): cls.bstack1ll1l1l1_opy_(driver)
            }
        })
    @classmethod
    def bstack1llll111_opy_(cls, event: str, bstack1l11ll1l_opy_: bstack1lll1l11_opy_):
        bstack1l1l1lll_opy_ = {
            bstack11l1l11_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭⇕"): event,
            bstack1l11ll1l_opy_.event_key(): bstack1l11ll1l_opy_.bstack11lll1ll_opy_(event)
        }
        cls.bstack1l1lll11_opy_(bstack1l1l1lll_opy_)
        result = getattr(bstack1l11ll1l_opy_, bstack11l1l11_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⇖"), None)
        if event == bstack11l1l11_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ⇗"):
            threading.current_thread().bstackTestMeta = {bstack11l1l11_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ⇘"): bstack11l1l11_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ⇙")}
        elif event == bstack11l1l11_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ⇚"):
            threading.current_thread().bstackTestMeta = {bstack11l1l11_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ⇛"): getattr(result, bstack11l1l11_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⇜"), bstack11l1l11_opy_ (u"ࠪࠫ⇝"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ⇞"), None) is None or os.environ[bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ⇟")] == bstack11l1l11_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ⇠")) and (os.environ.get(bstack11l1l11_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ⇡"), None) is None or os.environ[bstack11l1l11_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭⇢")] == bstack11l1l11_opy_ (u"ࠤࡱࡹࡱࡲࠢ⇣")):
            return False
        return True
    @staticmethod
    def bstack1llll1l1ll11_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l1lll1l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack11l1l11_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ⇤"): bstack11l1l11_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ⇥"),
            bstack11l1l11_opy_ (u"ࠬ࡞࠭ࡃࡕࡗࡅࡈࡑ࠭ࡕࡇࡖࡘࡔࡖࡓࠨ⇦"): bstack11l1l11_opy_ (u"࠭ࡴࡳࡷࡨࠫ⇧")
        }
        if os.environ.get(bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ⇨"), None):
            headers[bstack11l1l11_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨ⇩")] = bstack11l1l11_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬ⇪").format(os.environ[bstack11l1l11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠢ⇫")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack11l1l11_opy_ (u"ࠫࢀࢃ࠯ࡼࡿࠪ⇬").format(bstack1llll1l1111l_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack11l1l11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ⇭"), None)
    @staticmethod
    def bstack1ll1l1l1_opy_(driver):
        return {
            bstack111l111l1ll_opy_(): bstack1111ll111l1_opy_(driver)
        }
    @staticmethod
    def bstack1llll11ll1ll_opy_(exception_info, report):
        return [{bstack11l1l11_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩ⇮"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11111l111l_opy_(typename):
        if bstack11l1l11_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥ⇯") in typename:
            return bstack11l1l11_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤ⇰")
        return bstack11l1l11_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥ⇱")