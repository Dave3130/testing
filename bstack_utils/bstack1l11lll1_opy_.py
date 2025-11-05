# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111l1ll1111_opy_, bstack111l1l1lll1_opy_, bstack1l11l1111_opy_, error_handler, bstack1111l11lll1_opy_, bstack1111llll111_opy_, bstack1111llll11l_opy_, bstack1l111lll_opy_, bstack1ll111ll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l11l11111_opy_ import bstack111l1lll1l1_opy_
import bstack_utils.bstack1111ll11l1_opy_ as bstack11lll11lll_opy_
from bstack_utils.bstack1l1l111l_opy_ import bstack1l11111l_opy_
import bstack_utils.accessibility as bstack111ll1ll_opy_
from bstack_utils.bstack11111ll1l_opy_ import bstack11111ll1l_opy_
from bstack_utils.bstack1l1ll111_opy_ import bstack11lllll1_opy_
from bstack_utils.constants import bstack1l1llll11l_opy_
bstack1llll11l1111_opy_ = bstack1lll11l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡩ࡯࡭࡮ࡨࡧࡹࡵࡲ࠮ࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫℶ")
logger = logging.getLogger(__name__)
class bstack1l111l1l_opy_:
    bstack11l11l11111_opy_ = None
    bs_config = None
    bstack111l11l1l1_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l11lll11l_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def launch(cls, bs_config, bstack111l11l1l1_opy_):
        cls.bs_config = bs_config
        cls.bstack111l11l1l1_opy_ = bstack111l11l1l1_opy_
        try:
            cls.bstack1llll11l1ll1_opy_()
            bstack1llll1ll111l_opy_ = bstack111l1ll1111_opy_(bs_config)
            bstack1llll1lllll1_opy_ = bstack111l1l1lll1_opy_(bs_config)
            data = bstack11lll11lll_opy_.bstack1llll11ll111_opy_(bs_config, bstack111l11l1l1_opy_)
            config = {
                bstack1lll11l_opy_ (u"ࠬࡧࡵࡵࡪࠪℷ"): (bstack1llll1ll111l_opy_, bstack1llll1lllll1_opy_),
                bstack1lll11l_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧℸ"): cls.default_headers()
            }
            response = bstack1l11l1111_opy_(bstack1lll11l_opy_ (u"ࠧࡑࡑࡖࡘࠬℹ"), cls.request_url(bstack1lll11l_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠲࠰ࡤࡸ࡭ࡱࡪࡳࠨ℺")), data, config)
            if response.status_code != 200:
                bstack11llll1lll_opy_ = response.json()
                if bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ℻")] == False:
                    cls.bstack1llll11lllll_opy_(bstack11llll1lll_opy_)
                    return
                cls.bstack1llll11ll11l_opy_(bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪℼ")])
                cls.bstack1llll11llll1_opy_(bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫℽ")])
                return None
            bstack1llll11l1l1l_opy_ = cls.bstack1llll11lll1l_opy_(response)
            return bstack1llll11l1l1l_opy_, response.json()
        except Exception as error:
            logger.error(bstack1lll11l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡥࡹ࡮ࡲࡤࠡࡨࡲࡶ࡚ࠥࡥࡴࡶࡋࡹࡧࡀࠠࡼࡿࠥℾ").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll111ll1l_opy_=None):
        if not bstack1l11111l_opy_.on() and not bstack111ll1ll_opy_.on():
            return
        if os.environ.get(bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪℿ")) == bstack1lll11l_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ⅀") or os.environ.get(bstack1lll11l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭⅁")) == bstack1lll11l_opy_ (u"ࠤࡱࡹࡱࡲࠢ⅂"):
            logger.error(bstack1lll11l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡴࡶࠠࡣࡷ࡬ࡰࡩࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡡࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷ࡭ࡴࡴࠠࡵࡱ࡮ࡩࡳ࠭⅃"))
            return {
                bstack1lll11l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ⅄"): bstack1lll11l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫⅅ"),
                bstack1lll11l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧⅆ"): bstack1lll11l_opy_ (u"ࠧࡕࡱ࡮ࡩࡳ࠵ࡢࡶ࡫࡯ࡨࡎࡊࠠࡪࡵࠣࡹࡳࡪࡥࡧ࡫ࡱࡩࡩ࠲ࠠࡣࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡ࡯࡬࡫࡭ࡺࠠࡩࡣࡹࡩࠥ࡬ࡡࡪ࡮ࡨࡨࠬⅇ")
            }
        try:
            cls.bstack11l11l11111_opy_.shutdown()
            data = {
                bstack1lll11l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ⅈ"): bstack1l111lll_opy_()
            }
            if not bstack1llll111ll1l_opy_ is None:
                data[bstack1lll11l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡲ࡫ࡴࡢࡦࡤࡸࡦ࠭ⅉ")] = [{
                    bstack1lll11l_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪ⅊"): bstack1lll11l_opy_ (u"ࠫࡺࡹࡥࡳࡡ࡮࡭ࡱࡲࡥࡥࠩ⅋"),
                    bstack1lll11l_opy_ (u"ࠬࡹࡩࡨࡰࡤࡰࠬ⅌"): bstack1llll111ll1l_opy_
                }]
            config = {
                bstack1lll11l_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ⅍"): cls.default_headers()
            }
            bstack11ll111l1ll_opy_ = bstack1lll11l_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡷࡹࡵࡰࠨⅎ").format(os.environ[bstack1lll11l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨ⅏")])
            bstack1llll111lll1_opy_ = cls.request_url(bstack11ll111l1ll_opy_)
            response = bstack1l11l1111_opy_(bstack1lll11l_opy_ (u"ࠩࡓ࡙࡙࠭⅐"), bstack1llll111lll1_opy_, data, config)
            if not response.ok:
                raise Exception(bstack1lll11l_opy_ (u"ࠥࡗࡹࡵࡰࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡱࡳࡹࠦ࡯࡬ࠤ⅑"))
        except Exception as error:
            logger.error(bstack1lll11l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡵࡰࠡࡤࡸ࡭ࡱࡪࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤ࡙࡫ࡳࡵࡊࡸࡦ࠿ࡀࠠࠣ⅒") + str(error))
            return {
                bstack1lll11l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ⅓"): bstack1lll11l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ⅔"),
                bstack1lll11l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⅕"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11lll1l_opy_(cls, response):
        bstack11llll1lll_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll11l1l1l_opy_ = {}
        if bstack11llll1lll_opy_.get(bstack1lll11l_opy_ (u"ࠨ࡬ࡺࡸࠬ⅖")) is None:
            os.environ[bstack1lll11l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭⅗")] = bstack1lll11l_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ⅘")
        else:
            os.environ[bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ⅙")] = bstack11llll1lll_opy_.get(bstack1lll11l_opy_ (u"ࠬࡰࡷࡵࠩ⅚"), bstack1lll11l_opy_ (u"࠭࡮ࡶ࡮࡯ࠫ⅛"))
        os.environ[bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ⅜")] = bstack11llll1lll_opy_.get(bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ⅝"), bstack1lll11l_opy_ (u"ࠩࡱࡹࡱࡲࠧ⅞"))
        logger.info(bstack1lll11l_opy_ (u"ࠪࡘࡪࡹࡴࡩࡷࡥࠤࡸࡺࡡࡳࡶࡨࡨࠥࡽࡩࡵࡪࠣ࡭ࡩࡀࠠࠨ⅟") + os.getenv(bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩⅠ")));
        if bstack1l11111l_opy_.bstack11l111ll1l1_opy_(cls.bs_config, cls.bstack111l11l1l1_opy_.get(bstack1lll11l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡷࡶࡩࡩ࠭Ⅱ"), bstack1lll11l_opy_ (u"࠭ࠧⅢ"))) is True:
            bstack11ll111l1l1_opy_, build_hashed_id, bstack1llll111ll11_opy_ = cls.bstack1llll1l11111_opy_(bstack11llll1lll_opy_)
            if bstack11ll111l1l1_opy_ != None and build_hashed_id != None:
                bstack1llll11l1l1l_opy_[bstack1lll11l_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧⅣ")] = {
                    bstack1lll11l_opy_ (u"ࠨ࡬ࡺࡸࡤࡺ࡯࡬ࡧࡱࠫⅤ"): bstack11ll111l1l1_opy_,
                    bstack1lll11l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫⅥ"): build_hashed_id,
                    bstack1lll11l_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧⅦ"): bstack1llll111ll11_opy_
                }
            else:
                bstack1llll11l1l1l_opy_[bstack1lll11l_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫⅧ")] = {}
        else:
            bstack1llll11l1l1l_opy_[bstack1lll11l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬⅨ")] = {}
        bstack1llll11l11l1_opy_, build_hashed_id = cls.bstack1llll11l11ll_opy_(bstack11llll1lll_opy_)
        if bstack1llll11l11l1_opy_ != None and build_hashed_id != None:
            bstack1llll11l1l1l_opy_[bstack1lll11l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭Ⅹ")] = {
                bstack1lll11l_opy_ (u"ࠧࡢࡷࡷ࡬ࡤࡺ࡯࡬ࡧࡱࠫⅪ"): bstack1llll11l11l1_opy_,
                bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪⅫ"): build_hashed_id,
            }
        else:
            bstack1llll11l1l1l_opy_[bstack1lll11l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩⅬ")] = {}
        if bstack1llll11l1l1l_opy_[bstack1lll11l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪⅭ")].get(bstack1lll11l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭Ⅾ")) != None or bstack1llll11l1l1l_opy_[bstack1lll11l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬⅯ")].get(bstack1lll11l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨⅰ")) != None:
            cls.bstack1llll11ll1ll_opy_(bstack11llll1lll_opy_.get(bstack1lll11l_opy_ (u"ࠧ࡫ࡹࡷࠫⅱ")), bstack11llll1lll_opy_.get(bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪⅲ")))
        return bstack1llll11l1l1l_opy_
    @classmethod
    def bstack1llll1l11111_opy_(cls, bstack11llll1lll_opy_):
        if bstack11llll1lll_opy_.get(bstack1lll11l_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩⅳ")) == None:
            cls.bstack1llll11ll11l_opy_()
            return [None, None, None]
        if bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪⅴ")][bstack1lll11l_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬⅵ")] != True:
            cls.bstack1llll11ll11l_opy_(bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬⅶ")])
            return [None, None, None]
        logger.debug(bstack1lll11l_opy_ (u"࠭ࡻࡾࠢࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲࠡࠨⅷ").format(bstack1l1llll11l_opy_))
        os.environ[bstack1lll11l_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡇࡔࡓࡐࡍࡇࡗࡉࡉ࠭ⅸ")] = bstack1lll11l_opy_ (u"ࠨࡶࡵࡹࡪ࠭ⅹ")
        if bstack11llll1lll_opy_.get(bstack1lll11l_opy_ (u"ࠩ࡭ࡻࡹ࠭ⅺ")):
            os.environ[bstack1lll11l_opy_ (u"ࠪࡇࡗࡋࡄࡆࡐࡗࡍࡆࡒࡓࡠࡈࡒࡖࡤࡉࡒࡂࡕࡋࡣࡗࡋࡐࡐࡔࡗࡍࡓࡍࠧⅻ")] = json.dumps({
                bstack1lll11l_opy_ (u"ࠫࡺࡹࡥࡳࡰࡤࡱࡪ࠭ⅼ"): bstack111l1ll1111_opy_(cls.bs_config),
                bstack1lll11l_opy_ (u"ࠬࡶࡡࡴࡵࡺࡳࡷࡪࠧⅽ"): bstack111l1l1lll1_opy_(cls.bs_config)
            })
        if bstack11llll1lll_opy_.get(bstack1lll11l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨⅾ")):
            os.environ[bstack1lll11l_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭ⅿ")] = bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪↀ")]
        if bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩↁ")].get(bstack1lll11l_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫↂ"), {}).get(bstack1lll11l_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨↃ")):
            os.environ[bstack1lll11l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭ↄ")] = str(bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ↅ")][bstack1lll11l_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨↆ")][bstack1lll11l_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬↇ")])
        else:
            os.environ[bstack1lll11l_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡁࡍࡎࡒ࡛ࡤ࡙ࡃࡓࡇࡈࡒࡘࡎࡏࡕࡕࠪↈ")] = bstack1lll11l_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ↉")
        return [bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠫ࡯ࡽࡴࠨ↊")], bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ↋")], os.environ[bstack1lll11l_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧ↌")]]
    @classmethod
    def bstack1llll11l11ll_opy_(cls, bstack11llll1lll_opy_):
        if bstack11llll1lll_opy_.get(bstack1lll11l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ↍")) == None:
            cls.bstack1llll11llll1_opy_()
            return [None, None]
        if bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ↎")][bstack1lll11l_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ↏")] != True:
            cls.bstack1llll11llll1_opy_(bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ←")])
            return [None, None]
        if bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ↑")].get(bstack1lll11l_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭→")):
            logger.debug(bstack1lll11l_opy_ (u"࠭ࡔࡦࡵࡷࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡇࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲ࡙ࠥࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠣࠪ↓"))
            parsed = json.loads(os.getenv(bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ↔"), bstack1lll11l_opy_ (u"ࠨࡽࢀࠫ↕")))
            capabilities = bstack11lll11lll_opy_.bstack1llll11l1l11_opy_(bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ↖")][bstack1lll11l_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ↗")][bstack1lll11l_opy_ (u"ࠫࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ↘")], bstack1lll11l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ↙"), bstack1lll11l_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬ↚"))
            bstack1llll11l11l1_opy_ = capabilities[bstack1lll11l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡔࡰ࡭ࡨࡲࠬ↛")]
            os.environ[bstack1lll11l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭↜")] = bstack1llll11l11l1_opy_
            if bstack1lll11l_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨࠦ↝") in bstack11llll1lll_opy_ and bstack11llll1lll_opy_.get(bstack1lll11l_opy_ (u"ࠥࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠤ↞")) is None:
                parsed[bstack1lll11l_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ↟")] = capabilities[bstack1lll11l_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭↠")]
            os.environ[bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ↡")] = json.dumps(parsed)
            scripts = bstack11lll11lll_opy_.bstack1llll11l1l11_opy_(bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ↢")][bstack1lll11l_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩ↣")][bstack1lll11l_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪ↤")], bstack1lll11l_opy_ (u"ࠪࡲࡦࡳࡥࠨ↥"), bstack1lll11l_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࠬ↦"))
            bstack11111ll1l_opy_.bstack1l11llllll_opy_(scripts)
            commands = bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ↧")][bstack1lll11l_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ↨")][bstack1lll11l_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࡖࡲ࡛ࡷࡧࡰࠨ↩")].get(bstack1lll11l_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࠪ↪"))
            bstack11111ll1l_opy_.bstack1lllll1111l1_opy_(commands)
            bstack1lllll11111l_opy_ = capabilities.get(bstack1lll11l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ↫"))
            bstack11111ll1l_opy_.bstack1lllll1111ll_opy_(bstack1lllll11111l_opy_)
            bstack11111ll1l_opy_.store()
        return [bstack1llll11l11l1_opy_, bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ↬")]]
    @classmethod
    def bstack1llll11ll11l_opy_(cls, response=None):
        os.environ[bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ↭")] = bstack1lll11l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ↮")
        os.environ[bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ↯")] = bstack1lll11l_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬ↰")
        os.environ[bstack1lll11l_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡈࡕࡍࡑࡎࡈࡘࡊࡊࠧ↱")] = bstack1lll11l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ↲")
        os.environ[bstack1lll11l_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩ↳")] = bstack1lll11l_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ↴")
        os.environ[bstack1lll11l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡄࡐࡑࡕࡗࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࡘ࠭↵")] = bstack1lll11l_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ↶")
        cls.bstack1llll11lllll_opy_(response, bstack1lll11l_opy_ (u"ࠢࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠢ↷"))
        return [None, None, None]
    @classmethod
    def bstack1llll11llll1_opy_(cls, response=None):
        os.environ[bstack1lll11l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭↸")] = bstack1lll11l_opy_ (u"ࠩࡱࡹࡱࡲࠧ↹")
        os.environ[bstack1lll11l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ↺")] = bstack1lll11l_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ↻")
        os.environ[bstack1lll11l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ↼")] = bstack1lll11l_opy_ (u"࠭࡮ࡶ࡮࡯ࠫ↽")
        cls.bstack1llll11lllll_opy_(response, bstack1lll11l_opy_ (u"ࠢࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠢ↾"))
        return [None, None, None]
    @classmethod
    def bstack1llll11ll1ll_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack1lll11l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ↿")] = jwt
        os.environ[bstack1lll11l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ⇀")] = build_hashed_id
    @classmethod
    def bstack1llll11lllll_opy_(cls, response=None, product=bstack1lll11l_opy_ (u"ࠥࠦ⇁")):
        if response == None or response.get(bstack1lll11l_opy_ (u"ࠫࡪࡸࡲࡰࡴࡶࠫ⇂")) == None:
            logger.error(product + bstack1lll11l_opy_ (u"ࠧࠦࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠢ⇃"))
            return
        for error in response[bstack1lll11l_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭⇄")]:
            bstack1111l11ll1l_opy_ = error[bstack1lll11l_opy_ (u"ࠧ࡬ࡧࡼࠫ⇅")]
            error_message = error[bstack1lll11l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⇆")]
            if error_message:
                if bstack1111l11ll1l_opy_ == bstack1lll11l_opy_ (u"ࠤࡈࡖࡗࡕࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡆࡈࡒࡎࡋࡄࠣ⇇"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack1lll11l_opy_ (u"ࠥࡈࡦࡺࡡࠡࡷࡳࡰࡴࡧࡤࠡࡶࡲࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࠦ⇈") + product + bstack1lll11l_opy_ (u"ࠦࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡪࡵࡦࠢࡷࡳࠥࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠤ⇉"))
    @classmethod
    def bstack1llll11l1ll1_opy_(cls):
        if cls.bstack11l11l11111_opy_ is not None:
            return
        cls.bstack11l11l11111_opy_ = bstack111l1lll1l1_opy_(cls.post_data)
        cls.bstack11l11l11111_opy_.start()
    @classmethod
    def bstack1llll1l1_opy_(cls):
        if cls.bstack11l11l11111_opy_ is None:
            return
        cls.bstack11l11l11111_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1l111ll1_opy_, event_url=bstack1lll11l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡡࡵࡥ࡫ࠫ⇊")):
        config = {
            bstack1lll11l_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ⇋"): cls.default_headers()
        }
        logger.debug(bstack1lll11l_opy_ (u"ࠢࡱࡱࡶࡸࡤࡪࡡࡵࡣ࠽ࠤࡘ࡫࡮ࡥ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡸࡴࠦࡴࡦࡵࡷ࡬ࡺࡨࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶࡶࠤࢀࢃࠢ⇌").format(bstack1lll11l_opy_ (u"ࠨ࠮ࠣࠫ⇍").join([event[bstack1lll11l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭⇎")] for event in bstack1l111ll1_opy_])))
        response = bstack1l11l1111_opy_(bstack1lll11l_opy_ (u"ࠪࡔࡔ࡙ࡔࠨ⇏"), cls.request_url(event_url), bstack1l111ll1_opy_, config)
        bstack1llll1l1llll_opy_ = response.json()
    @classmethod
    def bstack1lll1l1l_opy_(cls, bstack1l111ll1_opy_, event_url=bstack1lll11l_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪ⇐")):
        logger.debug(bstack1lll11l_opy_ (u"ࠧࡹࡥ࡯ࡦࡢࡨࡦࡺࡡ࠻ࠢࡄࡸࡹ࡫࡭ࡱࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡤࡨࡩࠦࡤࡢࡶࡤࠤࡹࡵࠠࡣࡣࡷࡧ࡭ࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥ࠻ࠢࡾࢁࠧ⇑").format(bstack1l111ll1_opy_[bstack1lll11l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⇒")]))
        if not bstack11lll11lll_opy_.bstack1llll1l1111l_opy_(bstack1l111ll1_opy_[bstack1lll11l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ⇓")]):
            logger.debug(bstack1lll11l_opy_ (u"ࠣࡵࡨࡲࡩࡥࡤࡢࡶࡤ࠾ࠥࡔ࡯ࡵࠢࡤࡨࡩ࡯࡮ࡨࠢࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨ⇔").format(bstack1l111ll1_opy_[bstack1lll11l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭⇕")]))
            return
        bstack11llll1l1_opy_ = bstack11lll11lll_opy_.bstack1llll11l111l_opy_(bstack1l111ll1_opy_[bstack1lll11l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ⇖")], bstack1l111ll1_opy_.get(bstack1lll11l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭⇗")))
        if bstack11llll1l1_opy_ != None:
            if bstack1l111ll1_opy_.get(bstack1lll11l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧ⇘")) != None:
                bstack1l111ll1_opy_[bstack1lll11l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨ⇙")][bstack1lll11l_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ⇚")] = bstack11llll1l1_opy_
            else:
                bstack1l111ll1_opy_[bstack1lll11l_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭⇛")] = bstack11llll1l1_opy_
        if event_url == bstack1lll11l_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨ⇜"):
            cls.bstack1llll11l1ll1_opy_()
            logger.debug(bstack1lll11l_opy_ (u"ࠥࡷࡪࡴࡤࡠࡦࡤࡸࡦࡀࠠࡂࡦࡧ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥࡺ࡯ࠡࡤࡤࡸࡨ࡮ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨ⇝").format(bstack1l111ll1_opy_[bstack1lll11l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⇞")]))
            cls.bstack11l11l11111_opy_.add(bstack1l111ll1_opy_)
        elif event_url == bstack1lll11l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪ⇟"):
            cls.post_data([bstack1l111ll1_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1l11llll_opy_(cls, logs):
        for log in logs:
            bstack1llll11lll11_opy_ = {
                bstack1lll11l_opy_ (u"࠭࡫ࡪࡰࡧࠫ⇠"): bstack1lll11l_opy_ (u"ࠧࡕࡇࡖࡘࡤࡒࡏࡈࠩ⇡"),
                bstack1lll11l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ⇢"): log[bstack1lll11l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ⇣")],
                bstack1lll11l_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭⇤"): log[bstack1lll11l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ⇥")],
                bstack1lll11l_opy_ (u"ࠬ࡮ࡴࡵࡲࡢࡶࡪࡹࡰࡰࡰࡶࡩࠬ⇦"): {},
                bstack1lll11l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⇧"): log[bstack1lll11l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⇨")],
            }
            if bstack1lll11l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇩") in log:
                bstack1llll11lll11_opy_[bstack1lll11l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇪")] = log[bstack1lll11l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇫")]
            elif bstack1lll11l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇬") in log:
                bstack1llll11lll11_opy_[bstack1lll11l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⇭")] = log[bstack1lll11l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇮")]
            cls.bstack1lll1l1l_opy_({
                bstack1lll11l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ⇯"): bstack1lll11l_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬ⇰"),
                bstack1lll11l_opy_ (u"ࠩ࡯ࡳ࡬ࡹࠧ⇱"): [bstack1llll11lll11_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll111l1ll_opy_(cls, steps):
        bstack1llll111llll_opy_ = []
        for step in steps:
            bstack1llll1l111l1_opy_ = {
                bstack1lll11l_opy_ (u"ࠪ࡯࡮ࡴࡤࠨ⇲"): bstack1lll11l_opy_ (u"࡙ࠫࡋࡓࡕࡡࡖࡘࡊࡖࠧ⇳"),
                bstack1lll11l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ⇴"): step[bstack1lll11l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ⇵")],
                bstack1lll11l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ⇶"): step[bstack1lll11l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ⇷")],
                bstack1lll11l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⇸"): step[bstack1lll11l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⇹")],
                bstack1lll11l_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭⇺"): step[bstack1lll11l_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧ⇻")]
            }
            if bstack1lll11l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇼") in step:
                bstack1llll1l111l1_opy_[bstack1lll11l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇽")] = step[bstack1lll11l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇾")]
            elif bstack1lll11l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇿") in step:
                bstack1llll1l111l1_opy_[bstack1lll11l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ∀")] = step[bstack1lll11l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ∁")]
            bstack1llll111llll_opy_.append(bstack1llll1l111l1_opy_)
        cls.bstack1lll1l1l_opy_({
            bstack1lll11l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ∂"): bstack1lll11l_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ∃"),
            bstack1lll11l_opy_ (u"ࠧ࡭ࡱࡪࡷࠬ∄"): bstack1llll111llll_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack111llll111_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
    def bstack1ll111lll1_opy_(cls, screenshot):
        cls.bstack1lll1l1l_opy_({
            bstack1lll11l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ∅"): bstack1lll11l_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭∆"),
            bstack1lll11l_opy_ (u"ࠪࡰࡴ࡭ࡳࠨ∇"): [{
                bstack1lll11l_opy_ (u"ࠫࡰ࡯࡮ࡥࠩ∈"): bstack1lll11l_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࠧ∉"),
                bstack1lll11l_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ∊"): datetime.datetime.utcnow().isoformat() + bstack1lll11l_opy_ (u"࡛ࠧࠩ∋"),
                bstack1lll11l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ∌"): screenshot[bstack1lll11l_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨ∍")],
                bstack1lll11l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ∎"): screenshot[bstack1lll11l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ∏")]
            }]
        }, event_url=bstack1lll11l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪ∐"))
    @classmethod
    @error_handler(class_method=True)
    def bstack1ll11l1ll1_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1lll1l1l_opy_({
            bstack1lll11l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ∑"): bstack1lll11l_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫ−"),
            bstack1lll11l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࠪ∓"): {
                bstack1lll11l_opy_ (u"ࠤࡸࡹ࡮ࡪࠢ∔"): cls.current_test_uuid(),
                bstack1lll11l_opy_ (u"ࠥ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠤ∕"): cls.bstack1ll1l111_opy_(driver)
            }
        })
    @classmethod
    def bstack1lll1111_opy_(cls, event: str, bstack1l111ll1_opy_: bstack11lllll1_opy_):
        bstack1lllll11_opy_ = {
            bstack1lll11l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ∖"): event,
            bstack1l111ll1_opy_.event_key(): bstack1l111ll1_opy_.bstack1l11l1l1_opy_(event)
        }
        cls.bstack1lll1l1l_opy_(bstack1lllll11_opy_)
        result = getattr(bstack1l111ll1_opy_, bstack1lll11l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ∗"), None)
        if event == bstack1lll11l_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ∘"):
            threading.current_thread().bstackTestMeta = {bstack1lll11l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ∙"): bstack1lll11l_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩ√")}
        elif event == bstack1lll11l_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ∛"):
            threading.current_thread().bstackTestMeta = {bstack1lll11l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ∜"): getattr(result, bstack1lll11l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ∝"), bstack1lll11l_opy_ (u"ࠬ࠭∞"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ∟"), None) is None or os.environ[bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ∠")] == bstack1lll11l_opy_ (u"ࠣࡰࡸࡰࡱࠨ∡")) and (os.environ.get(bstack1lll11l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ∢"), None) is None or os.environ[bstack1lll11l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ∣")] == bstack1lll11l_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ∤")):
            return False
        return True
    @staticmethod
    def bstack1llll11ll1l1_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l111l1l_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack1lll11l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ∥"): bstack1lll11l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ∦"),
            bstack1lll11l_opy_ (u"࡙ࠧ࠯ࡅࡗ࡙ࡇࡃࡌ࠯ࡗࡉࡘ࡚ࡏࡑࡕࠪ∧"): bstack1lll11l_opy_ (u"ࠨࡶࡵࡹࡪ࠭∨")
        }
        if os.environ.get(bstack1lll11l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭∩"), None):
            headers[bstack1lll11l_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪ∪")] = bstack1lll11l_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࢀࢃࠧ∫").format(os.environ[bstack1lll11l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠤ∬")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack1lll11l_opy_ (u"࠭ࡻࡾ࠱ࡾࢁࠬ∭").format(bstack1llll11l1111_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack1lll11l_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫ∮"), None)
    @staticmethod
    def bstack1ll1l111_opy_(driver):
        return {
            bstack1111l11lll1_opy_(): bstack1111llll111_opy_(driver)
        }
    @staticmethod
    def bstack1llll11l1lll_opy_(exception_info, report):
        return [{bstack1lll11l_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫ∯"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack1111111lll_opy_(typename):
        if bstack1lll11l_opy_ (u"ࠤࡄࡷࡸ࡫ࡲࡵ࡫ࡲࡲࠧ∰") in typename:
            return bstack1lll11l_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦ∱")
        return bstack1lll11l_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧ∲")