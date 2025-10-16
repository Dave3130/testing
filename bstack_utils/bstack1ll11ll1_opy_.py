# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack1111lll1ll1_opy_, bstack1111llll1l1_opy_, bstack11ll1llll_opy_, error_handler, bstack111l1lll1l1_opy_, bstack111l1ll1lll_opy_, bstack111ll11111l_opy_, bstack1lll1111_opy_, bstack1ll1ll11_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l11ll1111_opy_ import bstack111ll11l11l_opy_
import bstack_utils.bstack11l11l11l1_opy_ as bstack11l1l1ll1_opy_
from bstack_utils.bstack1llll1l1_opy_ import bstack1l11l1ll_opy_
import bstack_utils.accessibility as bstack11l11lll_opy_
from bstack_utils.bstack11111lll11_opy_ import bstack11111lll11_opy_
from bstack_utils.bstack1ll1l111_opy_ import bstack1l111l11_opy_
from bstack_utils.constants import bstack1ll1111ll_opy_
bstack1llll1l11l1l_opy_ = bstack1ll11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡧࡴࡲ࡬ࡦࡥࡷࡳࡷ࠳࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩ⃼")
logger = logging.getLogger(__name__)
class bstack1ll111l1_opy_:
    bstack11l11ll1111_opy_ = None
    bs_config = None
    bstack111l1l1l1l_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l1l111ll1_opy_, stage=STAGE.bstack1111l1111_opy_)
    def launch(cls, bs_config, bstack111l1l1l1l_opy_):
        cls.bs_config = bs_config
        cls.bstack111l1l1l1l_opy_ = bstack111l1l1l1l_opy_
        try:
            cls.bstack1llll1ll11l1_opy_()
            bstack1llll1lllll1_opy_ = bstack1111lll1ll1_opy_(bs_config)
            bstack1llll1llll11_opy_ = bstack1111llll1l1_opy_(bs_config)
            data = bstack11l1l1ll1_opy_.bstack1llll1l1111l_opy_(bs_config, bstack111l1l1l1l_opy_)
            config = {
                bstack1ll11_opy_ (u"ࠪࡥࡺࡺࡨࠨ⃽"): (bstack1llll1lllll1_opy_, bstack1llll1llll11_opy_),
                bstack1ll11_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ⃾"): cls.default_headers()
            }
            response = bstack11ll1llll_opy_(bstack1ll11_opy_ (u"ࠬࡖࡏࡔࡖࠪ⃿"), cls.request_url(bstack1ll11_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠷࠵ࡢࡶ࡫࡯ࡨࡸ࠭℀")), data, config)
            if response.status_code != 200:
                bstack111l1ll1l1_opy_ = response.json()
                if bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨ℁")] == False:
                    cls.bstack1llll1ll1111_opy_(bstack111l1ll1l1_opy_)
                    return
                cls.bstack1llll1l1llll_opy_(bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨℂ")])
                cls.bstack1llll11llll1_opy_(bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ℃")])
                return None
            bstack1llll1l1l1l1_opy_ = cls.bstack1llll1l11lll_opy_(response)
            return bstack1llll1l1l1l1_opy_, response.json()
        except Exception as error:
            logger.error(bstack1ll11_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࠦࡦࡰࡴࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࢁࡽࠣ℄").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll1l11ll1_opy_=None):
        if not bstack1l11l1ll_opy_.on() and not bstack11l11lll_opy_.on():
            return
        if os.environ.get(bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ℅")) == bstack1ll11_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ℆") or os.environ.get(bstack1ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫℇ")) == bstack1ll11_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ℈"):
            logger.error(bstack1ll11_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡶࡲࡴࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡺ࡯ࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࡑ࡮ࡹࡳࡪࡰࡪࠤࡦࡻࡴࡩࡧࡱࡸ࡮ࡩࡡࡵ࡫ࡲࡲࠥࡺ࡯࡬ࡧࡱࠫ℉"))
            return {
                bstack1ll11_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩℊ"): bstack1ll11_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩℋ"),
                bstack1ll11_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬℌ"): bstack1ll11_opy_ (u"࡚ࠬ࡯࡬ࡧࡱ࠳ࡧࡻࡩ࡭ࡦࡌࡈࠥ࡯ࡳࠡࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧ࠰ࠥࡨࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦ࡭ࡪࡩ࡫ࡸࠥ࡮ࡡࡷࡧࠣࡪࡦ࡯࡬ࡦࡦࠪℍ")
            }
        try:
            cls.bstack11l11ll1111_opy_.shutdown()
            data = {
                bstack1ll11_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫℎ"): bstack1lll1111_opy_()
            }
            if not bstack1llll1l11ll1_opy_ is None:
                data[bstack1ll11_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡰࡩࡹࡧࡤࡢࡶࡤࠫℏ")] = [{
                    bstack1ll11_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨℐ"): bstack1ll11_opy_ (u"ࠩࡸࡷࡪࡸ࡟࡬࡫࡯ࡰࡪࡪࠧℑ"),
                    bstack1ll11_opy_ (u"ࠪࡷ࡮࡭࡮ࡢ࡮ࠪℒ"): bstack1llll1l11ll1_opy_
                }]
            config = {
                bstack1ll11_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬℓ"): cls.default_headers()
            }
            bstack11ll11lll11_opy_ = bstack1ll11_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽ࠰ࡵࡷࡳࡵ࠭℔").format(os.environ[bstack1ll11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦℕ")])
            bstack1llll1l1ll1l_opy_ = cls.request_url(bstack11ll11lll11_opy_)
            response = bstack11ll1llll_opy_(bstack1ll11_opy_ (u"ࠧࡑࡗࡗࠫ№"), bstack1llll1l1ll1l_opy_, data, config)
            if not response.ok:
                raise Exception(bstack1ll11_opy_ (u"ࠣࡕࡷࡳࡵࠦࡲࡦࡳࡸࡩࡸࡺࠠ࡯ࡱࡷࠤࡴࡱࠢ℗"))
        except Exception as error:
            logger.error(bstack1ll11_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡷࡳࡵࠦࡢࡶ࡫࡯ࡨࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡗࡩࡸࡺࡈࡶࡤ࠽࠾ࠥࠨ℘") + str(error))
            return {
                bstack1ll11_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪℙ"): bstack1ll11_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪℚ"),
                bstack1ll11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ℛ"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll1l11lll_opy_(cls, response):
        bstack111l1ll1l1_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll1l1l1l1_opy_ = {}
        if bstack111l1ll1l1_opy_.get(bstack1ll11_opy_ (u"࠭ࡪࡸࡶࠪℜ")) is None:
            os.environ[bstack1ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫℝ")] = bstack1ll11_opy_ (u"ࠨࡰࡸࡰࡱ࠭℞")
        else:
            os.environ[bstack1ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭℟")] = bstack111l1ll1l1_opy_.get(bstack1ll11_opy_ (u"ࠪ࡮ࡼࡺࠧ℠"), bstack1ll11_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ℡"))
        os.environ[bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ™")] = bstack111l1ll1l1_opy_.get(bstack1ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ℣"), bstack1ll11_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬℤ"))
        logger.info(bstack1ll11_opy_ (u"ࠨࡖࡨࡷࡹ࡮ࡵࡣࠢࡶࡸࡦࡸࡴࡦࡦࠣࡻ࡮ࡺࡨࠡ࡫ࡧ࠾ࠥ࠭℥") + os.getenv(bstack1ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧΩ")));
        if bstack1l11l1ll_opy_.bstack11l11l1l1l1_opy_(cls.bs_config, cls.bstack111l1l1l1l_opy_.get(bstack1ll11_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡵࡴࡧࡧࠫ℧"), bstack1ll11_opy_ (u"ࠫࠬℨ"))) is True:
            bstack11ll11lll1l_opy_, build_hashed_id, bstack1llll1l1l111_opy_ = cls.bstack1llll1l1l1ll_opy_(bstack111l1ll1l1_opy_)
            if bstack11ll11lll1l_opy_ != None and build_hashed_id != None:
                bstack1llll1l1l1l1_opy_[bstack1ll11_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ℩")] = {
                    bstack1ll11_opy_ (u"࠭ࡪࡸࡶࡢࡸࡴࡱࡥ࡯ࠩK"): bstack11ll11lll1l_opy_,
                    bstack1ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩÅ"): build_hashed_id,
                    bstack1ll11_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬℬ"): bstack1llll1l1l111_opy_
                }
            else:
                bstack1llll1l1l1l1_opy_[bstack1ll11_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩℭ")] = {}
        else:
            bstack1llll1l1l1l1_opy_[bstack1ll11_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ℮")] = {}
        bstack1llll1l111l1_opy_, build_hashed_id = cls.bstack1llll1l1l11l_opy_(bstack111l1ll1l1_opy_)
        if bstack1llll1l111l1_opy_ != None and build_hashed_id != None:
            bstack1llll1l1l1l1_opy_[bstack1ll11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫℯ")] = {
                bstack1ll11_opy_ (u"ࠬࡧࡵࡵࡪࡢࡸࡴࡱࡥ࡯ࠩℰ"): bstack1llll1l111l1_opy_,
                bstack1ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨℱ"): build_hashed_id,
            }
        else:
            bstack1llll1l1l1l1_opy_[bstack1ll11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧℲ")] = {}
        if bstack1llll1l1l1l1_opy_[bstack1ll11_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨℳ")].get(bstack1ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫℴ")) != None or bstack1llll1l1l1l1_opy_[bstack1ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪℵ")].get(bstack1ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ℶ")) != None:
            cls.bstack1llll11lllll_opy_(bstack111l1ll1l1_opy_.get(bstack1ll11_opy_ (u"ࠬࡰࡷࡵࠩℷ")), bstack111l1ll1l1_opy_.get(bstack1ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨℸ")))
        return bstack1llll1l1l1l1_opy_
    @classmethod
    def bstack1llll1l1l1ll_opy_(cls, bstack111l1ll1l1_opy_):
        if bstack111l1ll1l1_opy_.get(bstack1ll11_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧℹ")) == None:
            cls.bstack1llll1l1llll_opy_()
            return [None, None, None]
        if bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ℺")][bstack1ll11_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ℻")] != True:
            cls.bstack1llll1l1llll_opy_(bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪℼ")])
            return [None, None, None]
        logger.debug(bstack1ll11_opy_ (u"ࠫࢀࢃࠠࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࠦ࠭ℽ").format(bstack1ll1111ll_opy_))
        os.environ[bstack1ll11_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡅࡒࡑࡕࡒࡅࡕࡇࡇࠫℾ")] = bstack1ll11_opy_ (u"࠭ࡴࡳࡷࡨࠫℿ")
        if bstack111l1ll1l1_opy_.get(bstack1ll11_opy_ (u"ࠧ࡫ࡹࡷࠫ⅀")):
            os.environ[bstack1ll11_opy_ (u"ࠨࡅࡕࡉࡉࡋࡎࡕࡋࡄࡐࡘࡥࡆࡐࡔࡢࡇࡗࡇࡓࡉࡡࡕࡉࡕࡕࡒࡕࡋࡑࡋࠬ⅁")] = json.dumps({
                bstack1ll11_opy_ (u"ࠩࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫ⅂"): bstack1111lll1ll1_opy_(cls.bs_config),
                bstack1ll11_opy_ (u"ࠪࡴࡦࡹࡳࡸࡱࡵࡨࠬ⅃"): bstack1111llll1l1_opy_(cls.bs_config)
            })
        if bstack111l1ll1l1_opy_.get(bstack1ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭⅄")):
            os.environ[bstack1ll11_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡊࡄࡗࡍࡋࡄࡠࡋࡇࠫⅅ")] = bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨⅆ")]
        if bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧⅇ")].get(bstack1ll11_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩⅈ"), {}).get(bstack1ll11_opy_ (u"ࠩࡤࡰࡱࡵࡷࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭ⅉ")):
            os.environ[bstack1ll11_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫ⅊")] = str(bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ⅋")][bstack1ll11_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭⅌")][bstack1ll11_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪ⅍")])
        else:
            os.environ[bstack1ll11_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡆࡒࡌࡐ࡙ࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࡓࠨⅎ")] = bstack1ll11_opy_ (u"ࠣࡰࡸࡰࡱࠨ⅏")
        return [bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠩ࡭ࡻࡹ࠭⅐")], bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ⅑")], os.environ[bstack1ll11_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡃࡏࡐࡔ࡝࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࡗࠬ⅒")]]
    @classmethod
    def bstack1llll1l1l11l_opy_(cls, bstack111l1ll1l1_opy_):
        if bstack111l1ll1l1_opy_.get(bstack1ll11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⅓")) == None:
            cls.bstack1llll11llll1_opy_()
            return [None, None]
        if bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⅔")][bstack1ll11_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨ⅕")] != True:
            cls.bstack1llll11llll1_opy_(bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⅖")])
            return [None, None]
        if bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⅗")].get(bstack1ll11_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ⅘")):
            logger.debug(bstack1ll11_opy_ (u"࡙ࠫ࡫ࡳࡵࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲࠡࠨ⅙"))
            parsed = json.loads(os.getenv(bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭⅚"), bstack1ll11_opy_ (u"࠭ࡻࡾࠩ⅛")))
            capabilities = bstack11l1l1ll1_opy_.bstack1llll11lll11_opy_(bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⅜")][bstack1ll11_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩ⅝")][bstack1ll11_opy_ (u"ࠩࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⅞")], bstack1ll11_opy_ (u"ࠪࡲࡦࡳࡥࠨ⅟"), bstack1ll11_opy_ (u"ࠫࡻࡧ࡬ࡶࡧࠪⅠ"))
            bstack1llll1l111l1_opy_ = capabilities[bstack1ll11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࡙ࡵ࡫ࡦࡰࠪⅡ")]
            os.environ[bstack1ll11_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫⅢ")] = bstack1llll1l111l1_opy_
            if bstack1ll11_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡦࠤⅣ") in bstack111l1ll1l1_opy_ and bstack111l1ll1l1_opy_.get(bstack1ll11_opy_ (u"ࠣࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠢⅤ")) is None:
                parsed[bstack1ll11_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪⅥ")] = capabilities[bstack1ll11_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫⅦ")]
            os.environ[bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬⅧ")] = json.dumps(parsed)
            scripts = bstack11l1l1ll1_opy_.bstack1llll11lll11_opy_(bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬⅨ")][bstack1ll11_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧⅩ")][bstack1ll11_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨⅪ")], bstack1ll11_opy_ (u"ࠨࡰࡤࡱࡪ࠭Ⅻ"), bstack1ll11_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࠪⅬ"))
            bstack11111lll11_opy_.bstack1l11l1llll_opy_(scripts)
            commands = bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪⅭ")][bstack1ll11_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬⅮ")][bstack1ll11_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࡔࡰ࡙ࡵࡥࡵ࠭Ⅿ")].get(bstack1ll11_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨⅰ"))
            bstack11111lll11_opy_.bstack1lllll1l1l1l_opy_(commands)
            bstack1lllll1l1l11_opy_ = capabilities.get(bstack1ll11_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬⅱ"))
            bstack11111lll11_opy_.bstack1lllll1l11l1_opy_(bstack1lllll1l1l11_opy_)
            bstack11111lll11_opy_.store()
        return [bstack1llll1l111l1_opy_, bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪⅲ")]]
    @classmethod
    def bstack1llll1l1llll_opy_(cls, response=None):
        os.environ[bstack1ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧⅳ")] = bstack1ll11_opy_ (u"ࠪࡲࡺࡲ࡬ࠨⅴ")
        os.environ[bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨⅵ")] = bstack1ll11_opy_ (u"ࠬࡴࡵ࡭࡮ࠪⅶ")
        os.environ[bstack1ll11_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡆࡓࡒࡖࡌࡆࡖࡈࡈࠬⅷ")] = bstack1ll11_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ⅸ")
        os.environ[bstack1ll11_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧⅹ")] = bstack1ll11_opy_ (u"ࠤࡱࡹࡱࡲࠢⅺ")
        os.environ[bstack1ll11_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫⅻ")] = bstack1ll11_opy_ (u"ࠦࡳࡻ࡬࡭ࠤⅼ")
        cls.bstack1llll1ll1111_opy_(response, bstack1ll11_opy_ (u"ࠧࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠧⅽ"))
        return [None, None, None]
    @classmethod
    def bstack1llll11llll1_opy_(cls, response=None):
        os.environ[bstack1ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫⅾ")] = bstack1ll11_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬⅿ")
        os.environ[bstack1ll11_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ↀ")] = bstack1ll11_opy_ (u"ࠩࡱࡹࡱࡲࠧↁ")
        os.environ[bstack1ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧↂ")] = bstack1ll11_opy_ (u"ࠫࡳࡻ࡬࡭ࠩↃ")
        cls.bstack1llll1ll1111_opy_(response, bstack1ll11_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠧↄ"))
        return [None, None, None]
    @classmethod
    def bstack1llll11lllll_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack1ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪↅ")] = jwt
        os.environ[bstack1ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬↆ")] = build_hashed_id
    @classmethod
    def bstack1llll1ll1111_opy_(cls, response=None, product=bstack1ll11_opy_ (u"ࠣࠤↇ")):
        if response == None or response.get(bstack1ll11_opy_ (u"ࠩࡨࡶࡷࡵࡲࡴࠩↈ")) == None:
            logger.error(product + bstack1ll11_opy_ (u"ࠥࠤࡇࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠧ↉"))
            return
        for error in response[bstack1ll11_opy_ (u"ࠫࡪࡸࡲࡰࡴࡶࠫ↊")]:
            bstack111l1l11l11_opy_ = error[bstack1ll11_opy_ (u"ࠬࡱࡥࡺࠩ↋")]
            error_message = error[bstack1ll11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ↌")]
            if error_message:
                if bstack111l1l11l11_opy_ == bstack1ll11_opy_ (u"ࠢࡆࡔࡕࡓࡗࡥࡁࡄࡅࡈࡗࡘࡥࡄࡆࡐࡌࡉࡉࠨ↍"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack1ll11_opy_ (u"ࠣࡆࡤࡸࡦࠦࡵࡱ࡮ࡲࡥࡩࠦࡴࡰࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࠤ↎") + product + bstack1ll11_opy_ (u"ࠤࠣࡪࡦ࡯࡬ࡦࡦࠣࡨࡺ࡫ࠠࡵࡱࠣࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠢ↏"))
    @classmethod
    def bstack1llll1ll11l1_opy_(cls):
        if cls.bstack11l11ll1111_opy_ is not None:
            return
        cls.bstack11l11ll1111_opy_ = bstack111ll11l11l_opy_(cls.post_data)
        cls.bstack11l11ll1111_opy_.start()
    @classmethod
    def bstack1l1111l1_opy_(cls):
        if cls.bstack11l11ll1111_opy_ is None:
            return
        cls.bstack11l11ll1111_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1llll111_opy_, event_url=bstack1ll11_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡦࡺࡣࡩࠩ←")):
        config = {
            bstack1ll11_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ↑"): cls.default_headers()
        }
        logger.debug(bstack1ll11_opy_ (u"ࠧࡶ࡯ࡴࡶࡢࡨࡦࡺࡡ࠻ࠢࡖࡩࡳࡪࡩ࡯ࡩࠣࡨࡦࡺࡡࠡࡶࡲࠤࡹ࡫ࡳࡵࡪࡸࡦࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴࡴࠢࡾࢁࠧ→").format(bstack1ll11_opy_ (u"࠭ࠬࠡࠩ↓").join([event[bstack1ll11_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ↔")] for event in bstack1llll111_opy_])))
        response = bstack11ll1llll_opy_(bstack1ll11_opy_ (u"ࠨࡒࡒࡗ࡙࠭↕"), cls.request_url(event_url), bstack1llll111_opy_, config)
        bstack1lllll1111l1_opy_ = response.json()
    @classmethod
    def bstack1l11ll1l_opy_(cls, bstack1llll111_opy_, event_url=bstack1ll11_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨ↖")):
        logger.debug(bstack1ll11_opy_ (u"ࠥࡷࡪࡴࡤࡠࡦࡤࡸࡦࡀࠠࡂࡶࡷࡩࡲࡶࡴࡪࡰࡪࠤࡹࡵࠠࡢࡦࡧࠤࡩࡧࡴࡢࠢࡷࡳࠥࡨࡡࡵࡥ࡫ࠤࡼ࡯ࡴࡩࠢࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪࡀࠠࡼࡿࠥ↗").format(bstack1llll111_opy_[bstack1ll11_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ↘")]))
        if not bstack11l1l1ll1_opy_.bstack1llll11lll1l_opy_(bstack1llll111_opy_[bstack1ll11_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ↙")]):
            logger.debug(bstack1ll11_opy_ (u"ࠨࡳࡦࡰࡧࡣࡩࡧࡴࡢ࠼ࠣࡒࡴࡺࠠࡢࡦࡧ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫࠺ࠡࡽࢀࠦ↚").format(bstack1llll111_opy_[bstack1ll11_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ↛")]))
            return
        bstack11llll1ll1_opy_ = bstack11l1l1ll1_opy_.bstack1llll11ll1ll_opy_(bstack1llll111_opy_[bstack1ll11_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ↜")], bstack1llll111_opy_.get(bstack1ll11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ↝")))
        if bstack11llll1ll1_opy_ != None:
            if bstack1llll111_opy_.get(bstack1ll11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬ↞")) != None:
                bstack1llll111_opy_[bstack1ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭↟")][bstack1ll11_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪ↠")] = bstack11llll1ll1_opy_
            else:
                bstack1llll111_opy_[bstack1ll11_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫ↡")] = bstack11llll1ll1_opy_
        if event_url == bstack1ll11_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡣࡷࡧ࡭࠭↢"):
            cls.bstack1llll1ll11l1_opy_()
            logger.debug(bstack1ll11_opy_ (u"ࠣࡵࡨࡲࡩࡥࡤࡢࡶࡤ࠾ࠥࡇࡤࡥ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡸࡴࠦࡢࡢࡶࡦ࡬ࠥࡽࡩࡵࡪࠣࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫࠺ࠡࡽࢀࠦ↣").format(bstack1llll111_opy_[bstack1ll11_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭↤")]))
            cls.bstack11l11ll1111_opy_.add(bstack1llll111_opy_)
        elif event_url == bstack1ll11_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨ↥"):
            cls.post_data([bstack1llll111_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1lllll11_opy_(cls, logs):
        for log in logs:
            bstack1llll1ll111l_opy_ = {
                bstack1ll11_opy_ (u"ࠫࡰ࡯࡮ࡥࠩ↦"): bstack1ll11_opy_ (u"࡚ࠬࡅࡔࡖࡢࡐࡔࡍࠧ↧"),
                bstack1ll11_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ↨"): log[bstack1ll11_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭↩")],
                bstack1ll11_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ↪"): log[bstack1ll11_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ↫")],
                bstack1ll11_opy_ (u"ࠪ࡬ࡹࡺࡰࡠࡴࡨࡷࡵࡵ࡮ࡴࡧࠪ↬"): {},
                bstack1ll11_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ↭"): log[bstack1ll11_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭↮")],
            }
            if bstack1ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭↯") in log:
                bstack1llll1ll111l_opy_[bstack1ll11_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ↰")] = log[bstack1ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ↱")]
            elif bstack1ll11_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ↲") in log:
                bstack1llll1ll111l_opy_[bstack1ll11_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ↳")] = log[bstack1ll11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ↴")]
            cls.bstack1l11ll1l_opy_({
                bstack1ll11_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ↵"): bstack1ll11_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ↶"),
                bstack1ll11_opy_ (u"ࠧ࡭ࡱࡪࡷࠬ↷"): [bstack1llll1ll111l_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll1l11111_opy_(cls, steps):
        bstack1llll1l11l11_opy_ = []
        for step in steps:
            bstack1llll1l1lll1_opy_ = {
                bstack1ll11_opy_ (u"ࠨ࡭࡬ࡲࡩ࠭↸"): bstack1ll11_opy_ (u"ࠩࡗࡉࡘ࡚࡟ࡔࡖࡈࡔࠬ↹"),
                bstack1ll11_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ↺"): step[bstack1ll11_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ↻")],
                bstack1ll11_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ↼"): step[bstack1ll11_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ↽")],
                bstack1ll11_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ↾"): step[bstack1ll11_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ↿")],
                bstack1ll11_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫ⇀"): step[bstack1ll11_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬ⇁")]
            }
            if bstack1ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇂") in step:
                bstack1llll1l1lll1_opy_[bstack1ll11_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⇃")] = step[bstack1ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇄")]
            elif bstack1ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇅") in step:
                bstack1llll1l1lll1_opy_[bstack1ll11_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇆")] = step[bstack1ll11_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇇")]
            bstack1llll1l11l11_opy_.append(bstack1llll1l1lll1_opy_)
        cls.bstack1l11ll1l_opy_({
            bstack1ll11_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ⇈"): bstack1ll11_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨ⇉"),
            bstack1ll11_opy_ (u"ࠬࡲ࡯ࡨࡵࠪ⇊"): bstack1llll1l11l11_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11llllll11_opy_, stage=STAGE.bstack1111l1111_opy_)
    def bstack1l1l1l111l_opy_(cls, screenshot):
        cls.bstack1l11ll1l_opy_({
            bstack1ll11_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⇋"): bstack1ll11_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫ⇌"),
            bstack1ll11_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭⇍"): [{
                bstack1ll11_opy_ (u"ࠩ࡮࡭ࡳࡪࠧ⇎"): bstack1ll11_opy_ (u"ࠪࡘࡊ࡙ࡔࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࠬ⇏"),
                bstack1ll11_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ⇐"): datetime.datetime.utcnow().isoformat() + bstack1ll11_opy_ (u"ࠬࡠࠧ⇑"),
                bstack1ll11_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⇒"): screenshot[bstack1ll11_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭⇓")],
                bstack1ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇔"): screenshot[bstack1ll11_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇕")]
            }]
        }, event_url=bstack1ll11_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨ⇖"))
    @classmethod
    @error_handler(class_method=True)
    def bstack1ll111ll1_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1l11ll1l_opy_({
            bstack1ll11_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⇗"): bstack1ll11_opy_ (u"ࠬࡉࡂࡕࡕࡨࡷࡸ࡯࡯࡯ࡅࡵࡩࡦࡺࡥࡥࠩ⇘"),
            bstack1ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨ⇙"): {
                bstack1ll11_opy_ (u"ࠢࡶࡷ࡬ࡨࠧ⇚"): cls.current_test_uuid(),
                bstack1ll11_opy_ (u"ࠣ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠢ⇛"): cls.bstack1l11111l_opy_(driver)
            }
        })
    @classmethod
    def bstack1l11l11l_opy_(cls, event: str, bstack1llll111_opy_: bstack1l111l11_opy_):
        bstack1lll11l1_opy_ = {
            bstack1ll11_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭⇜"): event,
            bstack1llll111_opy_.event_key(): bstack1llll111_opy_.bstack1l11l1l1_opy_(event)
        }
        cls.bstack1l11ll1l_opy_(bstack1lll11l1_opy_)
        result = getattr(bstack1llll111_opy_, bstack1ll11_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⇝"), None)
        if event == bstack1ll11_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ⇞"):
            threading.current_thread().bstackTestMeta = {bstack1ll11_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ⇟"): bstack1ll11_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ⇠")}
        elif event == bstack1ll11_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ⇡"):
            threading.current_thread().bstackTestMeta = {bstack1ll11_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ⇢"): getattr(result, bstack1ll11_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⇣"), bstack1ll11_opy_ (u"ࠪࠫ⇤"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ⇥"), None) is None or os.environ[bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ⇦")] == bstack1ll11_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ⇧")) and (os.environ.get(bstack1ll11_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ⇨"), None) is None or os.environ[bstack1ll11_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭⇩")] == bstack1ll11_opy_ (u"ࠤࡱࡹࡱࡲࠢ⇪")):
            return False
        return True
    @staticmethod
    def bstack1llll1l1ll11_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1ll111l1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack1ll11_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ⇫"): bstack1ll11_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ⇬"),
            bstack1ll11_opy_ (u"ࠬ࡞࠭ࡃࡕࡗࡅࡈࡑ࠭ࡕࡇࡖࡘࡔࡖࡓࠨ⇭"): bstack1ll11_opy_ (u"࠭ࡴࡳࡷࡨࠫ⇮")
        }
        if os.environ.get(bstack1ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ⇯"), None):
            headers[bstack1ll11_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨ⇰")] = bstack1ll11_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬ⇱").format(os.environ[bstack1ll11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠢ⇲")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack1ll11_opy_ (u"ࠫࢀࢃ࠯ࡼࡿࠪ⇳").format(bstack1llll1l11l1l_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack1ll11_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ⇴"), None)
    @staticmethod
    def bstack1l11111l_opy_(driver):
        return {
            bstack111l1lll1l1_opy_(): bstack111l1ll1lll_opy_(driver)
        }
    @staticmethod
    def bstack1llll1l111ll_opy_(exception_info, report):
        return [{bstack1ll11_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩ⇵"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11111l111l_opy_(typename):
        if bstack1ll11_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥ⇶") in typename:
            return bstack1ll11_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤ⇷")
        return bstack1ll11_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥ⇸")