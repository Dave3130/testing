# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack1111ll11111_opy_, bstack111l111ll11_opy_, bstack11l1l111l1_opy_, error_handler, bstack111l11lllll_opy_, bstack1111lll1ll1_opy_, bstack111l1lll1l1_opy_, bstack1l1111ll_opy_, bstack1l11l1l1_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l11l111l1_opy_ import bstack111ll111111_opy_
import bstack_utils.bstack11l1llll1l_opy_ as bstack1l1ll11lll_opy_
from bstack_utils.bstack1ll1ll11_opy_ import bstack1ll11l1l_opy_
import bstack_utils.accessibility as bstack1111ll1l_opy_
from bstack_utils.bstack11l11l11ll_opy_ import bstack11l11l11ll_opy_
from bstack_utils.bstack11lll1ll_opy_ import bstack1l1l11l1_opy_
from bstack_utils.constants import bstack1111ll1ll_opy_
bstack1llll1l11ll1_opy_ = bstack1lllll1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡥࡲࡰࡱ࡫ࡣࡵࡱࡵ࠱ࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧℝ")
logger = logging.getLogger(__name__)
class bstack1ll1l1l1_opy_:
    bstack11l11l111l1_opy_ = None
    bs_config = None
    bstack1l111l1111_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l1l111l11_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def launch(cls, bs_config, bstack1l111l1111_opy_):
        cls.bs_config = bs_config
        cls.bstack1l111l1111_opy_ = bstack1l111l1111_opy_
        try:
            cls.bstack1llll1l11l11_opy_()
            bstack1llll1llll1l_opy_ = bstack1111ll11111_opy_(bs_config)
            bstack1llll1ll11l1_opy_ = bstack111l111ll11_opy_(bs_config)
            data = bstack1l1ll11lll_opy_.bstack1llll11l1lll_opy_(bs_config, bstack1l111l1111_opy_)
            config = {
                bstack1lllll1l_opy_ (u"ࠨࡣࡸࡸ࡭࠭℞"): (bstack1llll1llll1l_opy_, bstack1llll1ll11l1_opy_),
                bstack1lllll1l_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪ℟"): cls.default_headers()
            }
            response = bstack11l1l111l1_opy_(bstack1lllll1l_opy_ (u"ࠪࡔࡔ࡙ࡔࠨ℠"), cls.request_url(bstack1lllll1l_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠵࠳ࡧࡻࡩ࡭ࡦࡶࠫ℡")), data, config)
            if response.status_code != 200:
                bstack1lll11l111_opy_ = response.json()
                if bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭™")] == False:
                    cls.bstack1llll1l11lll_opy_(bstack1lll11l111_opy_)
                    return
                cls.bstack1llll11l11ll_opy_(bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭℣")])
                cls.bstack1llll11ll111_opy_(bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧℤ")])
                return None
            bstack1llll11l1l11_opy_ = cls.bstack1llll1l111ll_opy_(response)
            return bstack1llll11l1l11_opy_, response.json()
        except Exception as error:
            logger.error(bstack1lllll1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࠤ࡫ࡵࡲࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࡿࢂࠨ℥").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll11l1111_opy_=None):
        if not bstack1ll11l1l_opy_.on() and not bstack1111ll1l_opy_.on():
            return
        if os.environ.get(bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭Ω")) == bstack1lllll1l_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ℧") or os.environ.get(bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩℨ")) == bstack1lllll1l_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ℩"):
            logger.error(bstack1lllll1l_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡰࡲࠣࡦࡺ࡯࡬ࡥࠢࡵࡩࡶࡻࡥࡴࡶࠣࡸࡴࠦࡔࡦࡵࡷࡌࡺࡨ࠺ࠡࡏ࡬ࡷࡸ࡯࡮ࡨࠢࡤࡹࡹ࡮ࡥ࡯ࡶ࡬ࡧࡦࡺࡩࡰࡰࠣࡸࡴࡱࡥ࡯ࠩK"))
            return {
                bstack1lllll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧÅ"): bstack1lllll1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧℬ"),
                bstack1lllll1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪℭ"): bstack1lllll1l_opy_ (u"ࠪࡘࡴࡱࡥ࡯࠱ࡥࡹ࡮ࡲࡤࡊࡆࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡪ࡮ࡴࡥࡥ࠮ࠣࡦࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤࡲ࡯ࡧࡩࡶࠣ࡬ࡦࡼࡥࠡࡨࡤ࡭ࡱ࡫ࡤࠨ℮")
            }
        try:
            cls.bstack11l11l111l1_opy_.shutdown()
            data = {
                bstack1lllll1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩℯ"): bstack1l1111ll_opy_()
            }
            if not bstack1llll11l1111_opy_ is None:
                data[bstack1lllll1l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟࡮ࡧࡷࡥࡩࡧࡴࡢࠩℰ")] = [{
                    bstack1lllll1l_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ℱ"): bstack1lllll1l_opy_ (u"ࠧࡶࡵࡨࡶࡤࡱࡩ࡭࡮ࡨࡨࠬℲ"),
                    bstack1lllll1l_opy_ (u"ࠨࡵ࡬࡫ࡳࡧ࡬ࠨℳ"): bstack1llll11l1111_opy_
                }]
            config = {
                bstack1lllll1l_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪℴ"): cls.default_headers()
            }
            bstack11ll11l1111_opy_ = bstack1lllll1l_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂ࠵ࡳࡵࡱࡳࠫℵ").format(os.environ[bstack1lllll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤℶ")])
            bstack1llll11ll11l_opy_ = cls.request_url(bstack11ll11l1111_opy_)
            response = bstack11l1l111l1_opy_(bstack1lllll1l_opy_ (u"ࠬࡖࡕࡕࠩℷ"), bstack1llll11ll11l_opy_, data, config)
            if not response.ok:
                raise Exception(bstack1lllll1l_opy_ (u"ࠨࡓࡵࡱࡳࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡴ࡯ࡵࠢࡲ࡯ࠧℸ"))
        except Exception as error:
            logger.error(bstack1lllll1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡵࡱࡳࠤࡧࡻࡩ࡭ࡦࠣࡶࡪࡷࡵࡦࡵࡷࠤࡹࡵࠠࡕࡧࡶࡸࡍࡻࡢ࠻࠼ࠣࠦℹ") + str(error))
            return {
                bstack1lllll1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ℺"): bstack1lllll1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ℻"),
                bstack1lllll1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫℼ"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll1l111ll_opy_(cls, response):
        bstack1lll11l111_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll11l1l11_opy_ = {}
        if bstack1lll11l111_opy_.get(bstack1lllll1l_opy_ (u"ࠫ࡯ࡽࡴࠨℽ")) is None:
            os.environ[bstack1lllll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩℾ")] = bstack1lllll1l_opy_ (u"࠭࡮ࡶ࡮࡯ࠫℿ")
        else:
            os.environ[bstack1lllll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ⅀")] = bstack1lll11l111_opy_.get(bstack1lllll1l_opy_ (u"ࠨ࡬ࡺࡸࠬ⅁"), bstack1lllll1l_opy_ (u"ࠩࡱࡹࡱࡲࠧ⅂"))
        os.environ[bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ⅃")] = bstack1lll11l111_opy_.get(bstack1lllll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭⅄"), bstack1lllll1l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪⅅ"))
        logger.info(bstack1lllll1l_opy_ (u"࠭ࡔࡦࡵࡷ࡬ࡺࡨࠠࡴࡶࡤࡶࡹ࡫ࡤࠡࡹ࡬ࡸ࡭ࠦࡩࡥ࠼ࠣࠫⅆ") + os.getenv(bstack1lllll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬⅇ")));
        if bstack1ll11l1l_opy_.bstack11l111lllll_opy_(cls.bs_config, cls.bstack1l111l1111_opy_.get(bstack1lllll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩⅈ"), bstack1lllll1l_opy_ (u"ࠩࠪⅉ"))) is True:
            bstack11ll111llll_opy_, build_hashed_id, bstack1llll11llll1_opy_ = cls.bstack1llll11lll1l_opy_(bstack1lll11l111_opy_)
            if bstack11ll111llll_opy_ != None and build_hashed_id != None:
                bstack1llll11l1l11_opy_[bstack1lllll1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ⅊")] = {
                    bstack1lllll1l_opy_ (u"ࠫ࡯ࡽࡴࡠࡶࡲ࡯ࡪࡴࠧ⅋"): bstack11ll111llll_opy_,
                    bstack1lllll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ⅌"): build_hashed_id,
                    bstack1lllll1l_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪ⅍"): bstack1llll11llll1_opy_
                }
            else:
                bstack1llll11l1l11_opy_[bstack1lllll1l_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧⅎ")] = {}
        else:
            bstack1llll11l1l11_opy_[bstack1lllll1l_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ⅏")] = {}
        bstack1llll11lll11_opy_, build_hashed_id = cls.bstack1llll11l11l1_opy_(bstack1lll11l111_opy_)
        if bstack1llll11lll11_opy_ != None and build_hashed_id != None:
            bstack1llll11l1l11_opy_[bstack1lllll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⅐")] = {
                bstack1lllll1l_opy_ (u"ࠪࡥࡺࡺࡨࡠࡶࡲ࡯ࡪࡴࠧ⅑"): bstack1llll11lll11_opy_,
                bstack1lllll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭⅒"): build_hashed_id,
            }
        else:
            bstack1llll11l1l11_opy_[bstack1lllll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⅓")] = {}
        if bstack1llll11l1l11_opy_[bstack1lllll1l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭⅔")].get(bstack1lllll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ⅕")) != None or bstack1llll11l1l11_opy_[bstack1lllll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⅖")].get(bstack1lllll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ⅗")) != None:
            cls.bstack1llll1l11l1l_opy_(bstack1lll11l111_opy_.get(bstack1lllll1l_opy_ (u"ࠪ࡮ࡼࡺࠧ⅘")), bstack1lll11l111_opy_.get(bstack1lllll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭⅙")))
        return bstack1llll11l1l11_opy_
    @classmethod
    def bstack1llll11lll1l_opy_(cls, bstack1lll11l111_opy_):
        if bstack1lll11l111_opy_.get(bstack1lllll1l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ⅚")) == None:
            cls.bstack1llll11l11ll_opy_()
            return [None, None, None]
        if bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭⅛")][bstack1lllll1l_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨ⅜")] != True:
            cls.bstack1llll11l11ll_opy_(bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ⅝")])
            return [None, None, None]
        logger.debug(bstack1lllll1l_opy_ (u"ࠩࡾࢁࠥࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠤࠫ⅞").format(bstack1111ll1ll_opy_))
        os.environ[bstack1lllll1l_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡃࡐࡏࡓࡐࡊ࡚ࡅࡅࠩ⅟")] = bstack1lllll1l_opy_ (u"ࠫࡹࡸࡵࡦࠩⅠ")
        if bstack1lll11l111_opy_.get(bstack1lllll1l_opy_ (u"ࠬࡰࡷࡵࠩⅡ")):
            os.environ[bstack1lllll1l_opy_ (u"࠭ࡃࡓࡇࡇࡉࡓ࡚ࡉࡂࡎࡖࡣࡋࡕࡒࡠࡅࡕࡅࡘࡎ࡟ࡓࡇࡓࡓࡗ࡚ࡉࡏࡉࠪⅢ")] = json.dumps({
                bstack1lllll1l_opy_ (u"ࠧࡶࡵࡨࡶࡳࡧ࡭ࡦࠩⅣ"): bstack1111ll11111_opy_(cls.bs_config),
                bstack1lllll1l_opy_ (u"ࠨࡲࡤࡷࡸࡽ࡯ࡳࡦࠪⅤ"): bstack111l111ll11_opy_(cls.bs_config)
            })
        if bstack1lll11l111_opy_.get(bstack1lllll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫⅥ")):
            os.environ[bstack1lllll1l_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩⅦ")] = bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭Ⅷ")]
        if bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬⅨ")].get(bstack1lllll1l_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧⅩ"), {}).get(bstack1lllll1l_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫⅪ")):
            os.environ[bstack1lllll1l_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡇࡌࡍࡑ࡚ࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࡔࠩⅫ")] = str(bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩⅬ")][bstack1lllll1l_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫⅭ")][bstack1lllll1l_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨⅮ")])
        else:
            os.environ[bstack1lllll1l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭Ⅿ")] = bstack1lllll1l_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦⅰ")
        return [bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠧ࡫ࡹࡷࠫⅱ")], bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪⅲ")], os.environ[bstack1lllll1l_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪⅳ")]]
    @classmethod
    def bstack1llll11l11l1_opy_(cls, bstack1lll11l111_opy_):
        if bstack1lll11l111_opy_.get(bstack1lllll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪⅴ")) == None:
            cls.bstack1llll11ll111_opy_()
            return [None, None]
        if bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫⅵ")][bstack1lllll1l_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭ⅶ")] != True:
            cls.bstack1llll11ll111_opy_(bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ⅷ")])
            return [None, None]
        if bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧⅸ")].get(bstack1lllll1l_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩⅹ")):
            logger.debug(bstack1lllll1l_opy_ (u"ࠩࡗࡩࡸࡺࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࠦ࠭ⅺ"))
            parsed = json.loads(os.getenv(bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫⅻ"), bstack1lllll1l_opy_ (u"ࠫࢀࢃࠧⅼ")))
            capabilities = bstack1l1ll11lll_opy_.bstack1llll11l1l1l_opy_(bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬⅽ")][bstack1lllll1l_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧⅾ")][bstack1lllll1l_opy_ (u"ࠧࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ⅿ")], bstack1lllll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ↀ"), bstack1lllll1l_opy_ (u"ࠩࡹࡥࡱࡻࡥࠨↁ"))
            bstack1llll11lll11_opy_ = capabilities[bstack1lllll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡗࡳࡰ࡫࡮ࠨↂ")]
            os.environ[bstack1lllll1l_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩↃ")] = bstack1llll11lll11_opy_
            if bstack1lllll1l_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫ࠢↄ") in bstack1lll11l111_opy_ and bstack1lll11l111_opy_.get(bstack1lllll1l_opy_ (u"ࠨࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠧↅ")) is None:
                parsed[bstack1lllll1l_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨↆ")] = capabilities[bstack1lllll1l_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩↇ")]
            os.environ[bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪↈ")] = json.dumps(parsed)
            scripts = bstack1l1ll11lll_opy_.bstack1llll11l1l1l_opy_(bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ↉")][bstack1lllll1l_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ↊")][bstack1lllll1l_opy_ (u"ࠬࡹࡣࡳ࡫ࡳࡸࡸ࠭↋")], bstack1lllll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ↌"), bstack1lllll1l_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࠨ↍"))
            bstack11l11l11ll_opy_.bstack11lll1lll_opy_(scripts)
            commands = bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ↎")][bstack1lllll1l_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪ↏")][bstack1lllll1l_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷ࡙ࡵࡗࡳࡣࡳࠫ←")].get(bstack1lllll1l_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭↑"))
            bstack11l11l11ll_opy_.bstack1lllll11l1l1_opy_(commands)
            bstack1lllll11l11l_opy_ = capabilities.get(bstack1lllll1l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ→"))
            bstack11l11l11ll_opy_.bstack1lllll11l111_opy_(bstack1lllll11l11l_opy_)
            bstack11l11l11ll_opy_.store()
        return [bstack1llll11lll11_opy_, bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ↓")]]
    @classmethod
    def bstack1llll11l11ll_opy_(cls, response=None):
        os.environ[bstack1lllll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ↔")] = bstack1lllll1l_opy_ (u"ࠨࡰࡸࡰࡱ࠭↕")
        os.environ[bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭↖")] = bstack1lllll1l_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ↗")
        os.environ[bstack1lllll1l_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡄࡑࡐࡔࡑࡋࡔࡆࡆࠪ↘")] = bstack1lllll1l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ↙")
        os.environ[bstack1lllll1l_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬ↚")] = bstack1lllll1l_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ↛")
        os.environ[bstack1lllll1l_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡇࡌࡍࡑ࡚ࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࡔࠩ↜")] = bstack1lllll1l_opy_ (u"ࠤࡱࡹࡱࡲࠢ↝")
        cls.bstack1llll1l11lll_opy_(response, bstack1lllll1l_opy_ (u"ࠥࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠥ↞"))
        return [None, None, None]
    @classmethod
    def bstack1llll11ll111_opy_(cls, response=None):
        os.environ[bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ↟")] = bstack1lllll1l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ↠")
        os.environ[bstack1lllll1l_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ↡")] = bstack1lllll1l_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬ↢")
        os.environ[bstack1lllll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ↣")] = bstack1lllll1l_opy_ (u"ࠩࡱࡹࡱࡲࠧ↤")
        cls.bstack1llll1l11lll_opy_(response, bstack1lllll1l_opy_ (u"ࠥࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠥ↥"))
        return [None, None, None]
    @classmethod
    def bstack1llll1l11l1l_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ↦")] = jwt
        os.environ[bstack1lllll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ↧")] = build_hashed_id
    @classmethod
    def bstack1llll1l11lll_opy_(cls, response=None, product=bstack1lllll1l_opy_ (u"ࠨࠢ↨")):
        if response == None or response.get(bstack1lllll1l_opy_ (u"ࠧࡦࡴࡵࡳࡷࡹࠧ↩")) == None:
            logger.error(product + bstack1lllll1l_opy_ (u"ࠣࠢࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡪࡦ࡯࡬ࡦࡦࠥ↪"))
            return
        for error in response[bstack1lllll1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࡴࠩ↫")]:
            bstack1111l11l111_opy_ = error[bstack1lllll1l_opy_ (u"ࠪ࡯ࡪࡿࠧ↬")]
            error_message = error[bstack1lllll1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ↭")]
            if error_message:
                if bstack1111l11l111_opy_ == bstack1lllll1l_opy_ (u"ࠧࡋࡒࡓࡑࡕࡣࡆࡉࡃࡆࡕࡖࡣࡉࡋࡎࡊࡇࡇࠦ↮"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack1lllll1l_opy_ (u"ࠨࡄࡢࡶࡤࠤࡺࡶ࡬ࡰࡣࡧࠤࡹࡵࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࠢ↯") + product + bstack1lllll1l_opy_ (u"ࠢࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡦࡸࡩࠥࡺ࡯ࠡࡵࡲࡱࡪࠦࡥࡳࡴࡲࡶࠧ↰"))
    @classmethod
    def bstack1llll1l11l11_opy_(cls):
        if cls.bstack11l11l111l1_opy_ is not None:
            return
        cls.bstack11l11l111l1_opy_ = bstack111ll111111_opy_(cls.post_data)
        cls.bstack11l11l111l1_opy_.start()
    @classmethod
    def bstack1l11lll1_opy_(cls):
        if cls.bstack11l11l111l1_opy_ is None:
            return
        cls.bstack11l11l111l1_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1l111lll_opy_, event_url=bstack1lllll1l_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡤࡸࡨ࡮ࠧ↱")):
        config = {
            bstack1lllll1l_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪ↲"): cls.default_headers()
        }
        logger.debug(bstack1lllll1l_opy_ (u"ࠥࡴࡴࡹࡴࡠࡦࡤࡸࡦࡀࠠࡔࡧࡱࡨ࡮ࡴࡧࠡࡦࡤࡸࡦࠦࡴࡰࠢࡷࡩࡸࡺࡨࡶࡤࠣࡪࡴࡸࠠࡦࡸࡨࡲࡹࡹࠠࡼࡿࠥ↳").format(bstack1lllll1l_opy_ (u"ࠫ࠱ࠦࠧ↴").join([event[bstack1lllll1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ↵")] for event in bstack1l111lll_opy_])))
        response = bstack11l1l111l1_opy_(bstack1lllll1l_opy_ (u"࠭ࡐࡐࡕࡗࠫ↶"), cls.request_url(event_url), bstack1l111lll_opy_, config)
        bstack1llll1l1ll1l_opy_ = response.json()
    @classmethod
    def bstack1l111111_opy_(cls, bstack1l111lll_opy_, event_url=bstack1lllll1l_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡣࡷࡧ࡭࠭↷")):
        logger.debug(bstack1lllll1l_opy_ (u"ࠣࡵࡨࡲࡩࡥࡤࡢࡶࡤ࠾ࠥࡇࡴࡵࡧࡰࡴࡹ࡯࡮ࡨࠢࡷࡳࠥࡧࡤࡥࠢࡧࡥࡹࡧࠠࡵࡱࠣࡦࡦࡺࡣࡩࠢࡺ࡭ࡹ࡮ࠠࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨ࠾ࠥࢁࡽࠣ↸").format(bstack1l111lll_opy_[bstack1lllll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭↹")]))
        if not bstack1l1ll11lll_opy_.bstack1llll1l111l1_opy_(bstack1l111lll_opy_[bstack1lllll1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ↺")]):
            logger.debug(bstack1lllll1l_opy_ (u"ࠦࡸ࡫࡮ࡥࡡࡧࡥࡹࡧ࠺ࠡࡐࡲࡸࠥࡧࡤࡥ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡻ࡮ࡺࡨࠡࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩ࠿ࠦࡻࡾࠤ↻").format(bstack1l111lll_opy_[bstack1lllll1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ↼")]))
            return
        bstack111l1lll1l_opy_ = bstack1l1ll11lll_opy_.bstack1llll11l111l_opy_(bstack1l111lll_opy_[bstack1lllll1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ↽")], bstack1l111lll_opy_.get(bstack1lllll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩ↾")))
        if bstack111l1lll1l_opy_ != None:
            if bstack1l111lll_opy_.get(bstack1lllll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪ↿")) != None:
                bstack1l111lll_opy_[bstack1lllll1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ⇀")][bstack1lllll1l_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࡣࡲࡧࡰࠨ⇁")] = bstack111l1lll1l_opy_
            else:
                bstack1l111lll_opy_[bstack1lllll1l_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࡤࡳࡡࡱࠩ⇂")] = bstack111l1lll1l_opy_
        if event_url == bstack1lllll1l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡡࡵࡥ࡫ࠫ⇃"):
            cls.bstack1llll1l11l11_opy_()
            logger.debug(bstack1lllll1l_opy_ (u"ࠨࡳࡦࡰࡧࡣࡩࡧࡴࡢ࠼ࠣࡅࡩࡪࡩ࡯ࡩࠣࡨࡦࡺࡡࠡࡶࡲࠤࡧࡧࡴࡤࡪࠣࡻ࡮ࡺࡨࠡࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩ࠿ࠦࡻࡾࠤ⇄").format(bstack1l111lll_opy_[bstack1lllll1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ⇅")]))
            cls.bstack11l11l111l1_opy_.add(bstack1l111lll_opy_)
        elif event_url == bstack1lllll1l_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭⇆"):
            cls.post_data([bstack1l111lll_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1ll1llll_opy_(cls, logs):
        for log in logs:
            bstack1llll11ll1ll_opy_ = {
                bstack1lllll1l_opy_ (u"ࠩ࡮࡭ࡳࡪࠧ⇇"): bstack1lllll1l_opy_ (u"ࠪࡘࡊ࡙ࡔࡠࡎࡒࡋࠬ⇈"),
                bstack1lllll1l_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ⇉"): log[bstack1lllll1l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ⇊")],
                bstack1lllll1l_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ⇋"): log[bstack1lllll1l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ⇌")],
                bstack1lllll1l_opy_ (u"ࠨࡪࡷࡸࡵࡥࡲࡦࡵࡳࡳࡳࡹࡥࠨ⇍"): {},
                bstack1lllll1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⇎"): log[bstack1lllll1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⇏")],
            }
            if bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇐") in log:
                bstack1llll11ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⇑")] = log[bstack1lllll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇒")]
            elif bstack1lllll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇓") in log:
                bstack1llll11ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇔")] = log[bstack1lllll1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇕")]
            cls.bstack1l111111_opy_({
                bstack1lllll1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ⇖"): bstack1lllll1l_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨ⇗"),
                bstack1lllll1l_opy_ (u"ࠬࡲ࡯ࡨࡵࠪ⇘"): [bstack1llll11ll1ll_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11lllll_opy_(cls, steps):
        bstack1llll1l1111l_opy_ = []
        for step in steps:
            bstack1llll11ll1l1_opy_ = {
                bstack1lllll1l_opy_ (u"࠭࡫ࡪࡰࡧࠫ⇙"): bstack1lllll1l_opy_ (u"ࠧࡕࡇࡖࡘࡤ࡙ࡔࡆࡒࠪ⇚"),
                bstack1lllll1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ⇛"): step[bstack1lllll1l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ⇜")],
                bstack1lllll1l_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭⇝"): step[bstack1lllll1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ⇞")],
                bstack1lllll1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭⇟"): step[bstack1lllll1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⇠")],
                bstack1lllll1l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩ⇡"): step[bstack1lllll1l_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪ⇢")]
            }
            if bstack1lllll1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇣") in step:
                bstack1llll11ll1l1_opy_[bstack1lllll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇤")] = step[bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇥")]
            elif bstack1lllll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⇦") in step:
                bstack1llll11ll1l1_opy_[bstack1lllll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇧")] = step[bstack1lllll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇨")]
            bstack1llll1l1111l_opy_.append(bstack1llll11ll1l1_opy_)
        cls.bstack1l111111_opy_({
            bstack1lllll1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ⇩"): bstack1lllll1l_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭⇪"),
            bstack1lllll1l_opy_ (u"ࠪࡰࡴ࡭ࡳࠨ⇫"): bstack1llll1l1111l_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack1l1l1lllll_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
    def bstack11111llll1_opy_(cls, screenshot):
        cls.bstack1l111111_opy_({
            bstack1lllll1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⇬"): bstack1lllll1l_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩ⇭"),
            bstack1lllll1l_opy_ (u"࠭࡬ࡰࡩࡶࠫ⇮"): [{
                bstack1lllll1l_opy_ (u"ࠧ࡬࡫ࡱࡨࠬ⇯"): bstack1lllll1l_opy_ (u"ࠨࡖࡈࡗ࡙ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࠪ⇰"),
                bstack1lllll1l_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ⇱"): datetime.datetime.utcnow().isoformat() + bstack1lllll1l_opy_ (u"ࠪ࡞ࠬ⇲"),
                bstack1lllll1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⇳"): screenshot[bstack1lllll1l_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࠫ⇴")],
                bstack1lllll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇵"): screenshot[bstack1lllll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇶")]
            }]
        }, event_url=bstack1lllll1l_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭⇷"))
    @classmethod
    @error_handler(class_method=True)
    def bstack1111ll11ll_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1l111111_opy_({
            bstack1lllll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭⇸"): bstack1lllll1l_opy_ (u"ࠪࡇࡇ࡚ࡓࡦࡵࡶ࡭ࡴࡴࡃࡳࡧࡤࡸࡪࡪࠧ⇹"),
            bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭⇺"): {
                bstack1lllll1l_opy_ (u"ࠧࡻࡵࡪࡦࠥ⇻"): cls.current_test_uuid(),
                bstack1lllll1l_opy_ (u"ࠨࡩ࡯ࡶࡨ࡫ࡷࡧࡴࡪࡱࡱࡷࠧ⇼"): cls.bstack1ll111l1_opy_(driver)
            }
        })
    @classmethod
    def bstack1lll11ll_opy_(cls, event: str, bstack1l111lll_opy_: bstack1l1l11l1_opy_):
        bstack1ll111ll_opy_ = {
            bstack1lllll1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ⇽"): event,
            bstack1l111lll_opy_.event_key(): bstack1l111lll_opy_.bstack1l11ll11_opy_(event)
        }
        cls.bstack1l111111_opy_(bstack1ll111ll_opy_)
        result = getattr(bstack1l111lll_opy_, bstack1lllll1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ⇾"), None)
        if event == bstack1lllll1l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ⇿"):
            threading.current_thread().bstackTestMeta = {bstack1lllll1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ∀"): bstack1lllll1l_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ∁")}
        elif event == bstack1lllll1l_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ∂"):
            threading.current_thread().bstackTestMeta = {bstack1lllll1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭∃"): getattr(result, bstack1lllll1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ∄"), bstack1lllll1l_opy_ (u"ࠨࠩ∅"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭∆"), None) is None or os.environ[bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ∇")] == bstack1lllll1l_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ∈")) and (os.environ.get(bstack1lllll1l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ∉"), None) is None or os.environ[bstack1lllll1l_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ∊")] == bstack1lllll1l_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ∋")):
            return False
        return True
    @staticmethod
    def bstack1llll11l1ll1_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1ll1l1l1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack1lllll1l_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧ∌"): bstack1lllll1l_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ∍"),
            bstack1lllll1l_opy_ (u"ࠪ࡜࠲ࡈࡓࡕࡃࡆࡏ࠲࡚ࡅࡔࡖࡒࡔࡘ࠭∎"): bstack1lllll1l_opy_ (u"ࠫࡹࡸࡵࡦࠩ∏")
        }
        if os.environ.get(bstack1lllll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ∐"), None):
            headers[bstack1lllll1l_opy_ (u"࠭ࡁࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭∑")] = bstack1lllll1l_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࡼࡿࠪ−").format(os.environ[bstack1lllll1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠧ∓")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack1lllll1l_opy_ (u"ࠩࡾࢁ࠴ࢁࡽࠨ∔").format(bstack1llll1l11ll1_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡࡸࡹ࡮ࡪࠧ∕"), None)
    @staticmethod
    def bstack1ll111l1_opy_(driver):
        return {
            bstack111l11lllll_opy_(): bstack1111lll1ll1_opy_(driver)
        }
    @staticmethod
    def bstack1llll1l11111_opy_(exception_info, report):
        return [{bstack1lllll1l_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧ∖"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack111111l111_opy_(typename):
        if bstack1lllll1l_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣ∗") in typename:
            return bstack1lllll1l_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢ∘")
        return bstack1lllll1l_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣ∙")