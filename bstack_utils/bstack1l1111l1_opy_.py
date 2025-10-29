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
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111l1l11l1l_opy_, bstack111l111l1l1_opy_, bstack1l1llllll_opy_, error_handler, bstack1111lll1ll1_opy_, bstack111l1ll1ll1_opy_, bstack1111ll1l1ll_opy_, bstack1l111ll1_opy_, bstack1lllll11_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l111lll11_opy_ import bstack111l1lll111_opy_
import bstack_utils.bstack11ll1ll1ll_opy_ as bstack1llll11l1l_opy_
from bstack_utils.bstack1llll1ll_opy_ import bstack1ll1llll_opy_
import bstack_utils.accessibility as bstack1lllll1l1_opy_
from bstack_utils.bstack1l1l111ll_opy_ import bstack1l1l111ll_opy_
from bstack_utils.bstack1l1l11l1_opy_ import bstack1ll1ll11_opy_
from bstack_utils.constants import bstack1l11llll1_opy_
bstack1llll1l1111l_opy_ = bstack11ll1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡧࡴࡲ࡬ࡦࡥࡷࡳࡷ࠳࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩ℻")
logger = logging.getLogger(__name__)
class bstack1l1l1lll_opy_:
    bstack11l111lll11_opy_ = None
    bs_config = None
    bstack11lll11l1l_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l11lll11l_opy_, stage=STAGE.bstack11ll11lll_opy_)
    def launch(cls, bs_config, bstack11lll11l1l_opy_):
        cls.bs_config = bs_config
        cls.bstack11lll11l1l_opy_ = bstack11lll11l1l_opy_
        try:
            cls.bstack1llll11ll111_opy_()
            bstack1llll1ll1l11_opy_ = bstack111l1l11l1l_opy_(bs_config)
            bstack1llll1lll1l1_opy_ = bstack111l111l1l1_opy_(bs_config)
            data = bstack1llll11l1l_opy_.bstack1llll11ll1ll_opy_(bs_config, bstack11lll11l1l_opy_)
            config = {
                bstack11ll1l_opy_ (u"ࠪࡥࡺࡺࡨࠨℼ"): (bstack1llll1ll1l11_opy_, bstack1llll1lll1l1_opy_),
                bstack11ll1l_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬℽ"): cls.default_headers()
            }
            response = bstack1l1llllll_opy_(bstack11ll1l_opy_ (u"ࠬࡖࡏࡔࡖࠪℾ"), cls.request_url(bstack11ll1l_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠷࠵ࡢࡶ࡫࡯ࡨࡸ࠭ℿ")), data, config)
            if response.status_code != 200:
                bstack11ll1ll11_opy_ = response.json()
                if bstack11ll1ll11_opy_[bstack11ll1l_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨ⅀")] == False:
                    cls.bstack1llll11lll1l_opy_(bstack11ll1ll11_opy_)
                    return
                cls.bstack1llll11l1l1l_opy_(bstack11ll1ll11_opy_[bstack11ll1l_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ⅁")])
                cls.bstack1llll11lll11_opy_(bstack11ll1ll11_opy_[bstack11ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⅂")])
                return None
            bstack1llll11l1111_opy_ = cls.bstack1llll111ll1l_opy_(response)
            return bstack1llll11l1111_opy_, response.json()
        except Exception as error:
            logger.error(bstack11ll1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࠦࡦࡰࡴࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࢁࡽࠣ⅃").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll111llll_opy_=None):
        if not bstack1ll1llll_opy_.on() and not bstack1lllll1l1_opy_.on():
            return
        if os.environ.get(bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ⅄")) == bstack11ll1l_opy_ (u"ࠧࡴࡵ࡭࡮ࠥⅅ") or os.environ.get(bstack11ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫⅆ")) == bstack11ll1l_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧⅇ"):
            logger.error(bstack11ll1l_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡶࡲࡴࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡺ࡯ࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࡑ࡮ࡹࡳࡪࡰࡪࠤࡦࡻࡴࡩࡧࡱࡸ࡮ࡩࡡࡵ࡫ࡲࡲࠥࡺ࡯࡬ࡧࡱࠫⅈ"))
            return {
                bstack11ll1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩⅉ"): bstack11ll1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ⅊"),
                bstack11ll1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⅋"): bstack11ll1l_opy_ (u"࡚ࠬ࡯࡬ࡧࡱ࠳ࡧࡻࡩ࡭ࡦࡌࡈࠥ࡯ࡳࠡࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧ࠰ࠥࡨࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦ࡭ࡪࡩ࡫ࡸࠥ࡮ࡡࡷࡧࠣࡪࡦ࡯࡬ࡦࡦࠪ⅌")
            }
        try:
            cls.bstack11l111lll11_opy_.shutdown()
            data = {
                bstack11ll1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⅍"): bstack1l111ll1_opy_()
            }
            if not bstack1llll111llll_opy_ is None:
                data[bstack11ll1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡰࡩࡹࡧࡤࡢࡶࡤࠫⅎ")] = [{
                    bstack11ll1l_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨ⅏"): bstack11ll1l_opy_ (u"ࠩࡸࡷࡪࡸ࡟࡬࡫࡯ࡰࡪࡪࠧ⅐"),
                    bstack11ll1l_opy_ (u"ࠪࡷ࡮࡭࡮ࡢ࡮ࠪ⅑"): bstack1llll111llll_opy_
                }]
            config = {
                bstack11ll1l_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ⅒"): cls.default_headers()
            }
            bstack11ll111l11l_opy_ = bstack11ll1l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽ࠰ࡵࡷࡳࡵ࠭⅓").format(os.environ[bstack11ll1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦ⅔")])
            bstack1llll11l1ll1_opy_ = cls.request_url(bstack11ll111l11l_opy_)
            response = bstack1l1llllll_opy_(bstack11ll1l_opy_ (u"ࠧࡑࡗࡗࠫ⅕"), bstack1llll11l1ll1_opy_, data, config)
            if not response.ok:
                raise Exception(bstack11ll1l_opy_ (u"ࠣࡕࡷࡳࡵࠦࡲࡦࡳࡸࡩࡸࡺࠠ࡯ࡱࡷࠤࡴࡱࠢ⅖"))
        except Exception as error:
            logger.error(bstack11ll1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡷࡳࡵࠦࡢࡶ࡫࡯ࡨࠥࡸࡥࡲࡷࡨࡷࡹࠦࡴࡰࠢࡗࡩࡸࡺࡈࡶࡤ࠽࠾ࠥࠨ⅗") + str(error))
            return {
                bstack11ll1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ⅘"): bstack11ll1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ⅙"),
                bstack11ll1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭⅚"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll111ll1l_opy_(cls, response):
        bstack11ll1ll11_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll11l1111_opy_ = {}
        if bstack11ll1ll11_opy_.get(bstack11ll1l_opy_ (u"࠭ࡪࡸࡶࠪ⅛")) is None:
            os.environ[bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ⅜")] = bstack11ll1l_opy_ (u"ࠨࡰࡸࡰࡱ࠭⅝")
        else:
            os.environ[bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭⅞")] = bstack11ll1ll11_opy_.get(bstack11ll1l_opy_ (u"ࠪ࡮ࡼࡺࠧ⅟"), bstack11ll1l_opy_ (u"ࠫࡳࡻ࡬࡭ࠩⅠ"))
        os.environ[bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪⅡ")] = bstack11ll1ll11_opy_.get(bstack11ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨⅢ"), bstack11ll1l_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬⅣ"))
        logger.info(bstack11ll1l_opy_ (u"ࠨࡖࡨࡷࡹ࡮ࡵࡣࠢࡶࡸࡦࡸࡴࡦࡦࠣࡻ࡮ࡺࡨࠡ࡫ࡧ࠾ࠥ࠭Ⅴ") + os.getenv(bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧⅥ")));
        if bstack1ll1llll_opy_.bstack11l111ll1ll_opy_(cls.bs_config, cls.bstack11lll11l1l_opy_.get(bstack11ll1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡵࡴࡧࡧࠫⅦ"), bstack11ll1l_opy_ (u"ࠫࠬⅧ"))) is True:
            bstack11ll111l1l1_opy_, build_hashed_id, bstack1llll11llll1_opy_ = cls.bstack1llll11l1l11_opy_(bstack11ll1ll11_opy_)
            if bstack11ll111l1l1_opy_ != None and build_hashed_id != None:
                bstack1llll11l1111_opy_[bstack11ll1l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬⅨ")] = {
                    bstack11ll1l_opy_ (u"࠭ࡪࡸࡶࡢࡸࡴࡱࡥ࡯ࠩⅩ"): bstack11ll111l1l1_opy_,
                    bstack11ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩⅪ"): build_hashed_id,
                    bstack11ll1l_opy_ (u"ࠨࡣ࡯ࡰࡴࡽ࡟ࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࡷࠬⅫ"): bstack1llll11llll1_opy_
                }
            else:
                bstack1llll11l1111_opy_[bstack11ll1l_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩⅬ")] = {}
        else:
            bstack1llll11l1111_opy_[bstack11ll1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪⅭ")] = {}
        bstack1llll11l11ll_opy_, build_hashed_id = cls.bstack1llll111ll11_opy_(bstack11ll1ll11_opy_)
        if bstack1llll11l11ll_opy_ != None and build_hashed_id != None:
            bstack1llll11l1111_opy_[bstack11ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫⅮ")] = {
                bstack11ll1l_opy_ (u"ࠬࡧࡵࡵࡪࡢࡸࡴࡱࡥ࡯ࠩⅯ"): bstack1llll11l11ll_opy_,
                bstack11ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨⅰ"): build_hashed_id,
            }
        else:
            bstack1llll11l1111_opy_[bstack11ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧⅱ")] = {}
        if bstack1llll11l1111_opy_[bstack11ll1l_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨⅲ")].get(bstack11ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫⅳ")) != None or bstack1llll11l1111_opy_[bstack11ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪⅴ")].get(bstack11ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ⅵ")) != None:
            cls.bstack1llll11ll1l1_opy_(bstack11ll1ll11_opy_.get(bstack11ll1l_opy_ (u"ࠬࡰࡷࡵࠩⅶ")), bstack11ll1ll11_opy_.get(bstack11ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨⅷ")))
        return bstack1llll11l1111_opy_
    @classmethod
    def bstack1llll11l1l11_opy_(cls, bstack11ll1ll11_opy_):
        if bstack11ll1ll11_opy_.get(bstack11ll1l_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧⅸ")) == None:
            cls.bstack1llll11l1l1l_opy_()
            return [None, None, None]
        if bstack11ll1ll11_opy_[bstack11ll1l_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨⅹ")][bstack11ll1l_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪⅺ")] != True:
            cls.bstack1llll11l1l1l_opy_(bstack11ll1ll11_opy_[bstack11ll1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪⅻ")])
            return [None, None, None]
        logger.debug(bstack11ll1l_opy_ (u"ࠫࢀࢃࠠࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࠦ࠭ⅼ").format(bstack1l11llll1_opy_))
        os.environ[bstack11ll1l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡅࡒࡑࡕࡒࡅࡕࡇࡇࠫⅽ")] = bstack11ll1l_opy_ (u"࠭ࡴࡳࡷࡨࠫⅾ")
        if bstack11ll1ll11_opy_.get(bstack11ll1l_opy_ (u"ࠧ࡫ࡹࡷࠫⅿ")):
            os.environ[bstack11ll1l_opy_ (u"ࠨࡅࡕࡉࡉࡋࡎࡕࡋࡄࡐࡘࡥࡆࡐࡔࡢࡇࡗࡇࡓࡉࡡࡕࡉࡕࡕࡒࡕࡋࡑࡋࠬↀ")] = json.dumps({
                bstack11ll1l_opy_ (u"ࠩࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫↁ"): bstack111l1l11l1l_opy_(cls.bs_config),
                bstack11ll1l_opy_ (u"ࠪࡴࡦࡹࡳࡸࡱࡵࡨࠬↂ"): bstack111l111l1l1_opy_(cls.bs_config)
            })
        if bstack11ll1ll11_opy_.get(bstack11ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭Ↄ")):
            os.environ[bstack11ll1l_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡊࡄࡗࡍࡋࡄࡠࡋࡇࠫↄ")] = bstack11ll1ll11_opy_[bstack11ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨↅ")]
        if bstack11ll1ll11_opy_[bstack11ll1l_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧↆ")].get(bstack11ll1l_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩↇ"), {}).get(bstack11ll1l_opy_ (u"ࠩࡤࡰࡱࡵࡷࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭ↈ")):
            os.environ[bstack11ll1l_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫ↉")] = str(bstack11ll1ll11_opy_[bstack11ll1l_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ↊")][bstack11ll1l_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭↋")][bstack11ll1l_opy_ (u"࠭ࡡ࡭࡮ࡲࡻࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࡵࠪ↌")])
        else:
            os.environ[bstack11ll1l_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡆࡒࡌࡐ࡙ࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࡓࠨ↍")] = bstack11ll1l_opy_ (u"ࠣࡰࡸࡰࡱࠨ↎")
        return [bstack11ll1ll11_opy_[bstack11ll1l_opy_ (u"ࠩ࡭ࡻࡹ࠭↏")], bstack11ll1ll11_opy_[bstack11ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ←")], os.environ[bstack11ll1l_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡃࡏࡐࡔ࡝࡟ࡔࡅࡕࡉࡊࡔࡓࡉࡑࡗࡗࠬ↑")]]
    @classmethod
    def bstack1llll111ll11_opy_(cls, bstack11ll1ll11_opy_):
        if bstack11ll1ll11_opy_.get(bstack11ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ→")) == None:
            cls.bstack1llll11lll11_opy_()
            return [None, None]
        if bstack11ll1ll11_opy_[bstack11ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭↓")][bstack11ll1l_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨ↔")] != True:
            cls.bstack1llll11lll11_opy_(bstack11ll1ll11_opy_[bstack11ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ↕")])
            return [None, None]
        if bstack11ll1ll11_opy_[bstack11ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ↖")].get(bstack11ll1l_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ↗")):
            logger.debug(bstack11ll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣࡗࡺࡩࡣࡦࡵࡶࡪࡺࡲࠡࠨ↘"))
            parsed = json.loads(os.getenv(bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭↙"), bstack11ll1l_opy_ (u"࠭ࡻࡾࠩ↚")))
            capabilities = bstack1llll11l1l_opy_.bstack1llll1l111ll_opy_(bstack11ll1ll11_opy_[bstack11ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ↛")][bstack11ll1l_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩ↜")][bstack11ll1l_opy_ (u"ࠩࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ↝")], bstack11ll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ↞"), bstack11ll1l_opy_ (u"ࠫࡻࡧ࡬ࡶࡧࠪ↟"))
            bstack1llll11l11ll_opy_ = capabilities[bstack11ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࡙ࡵ࡫ࡦࡰࠪ↠")]
            os.environ[bstack11ll1l_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ↡")] = bstack1llll11l11ll_opy_
            if bstack11ll1l_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡦࠤ↢") in bstack11ll1ll11_opy_ and bstack11ll1ll11_opy_.get(bstack11ll1l_opy_ (u"ࠣࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠢ↣")) is None:
                parsed[bstack11ll1l_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ↤")] = capabilities[bstack11ll1l_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ↥")]
            os.environ[bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ↦")] = json.dumps(parsed)
            scripts = bstack1llll11l1l_opy_.bstack1llll1l111ll_opy_(bstack11ll1ll11_opy_[bstack11ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ↧")][bstack11ll1l_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ↨")][bstack11ll1l_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨ↩")], bstack11ll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭↪"), bstack11ll1l_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࠪ↫"))
            bstack1l1l111ll_opy_.bstack111lll11l_opy_(scripts)
            commands = bstack11ll1ll11_opy_[bstack11ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ↬")][bstack11ll1l_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ↭")][bstack11ll1l_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࡔࡰ࡙ࡵࡥࡵ࠭↮")].get(bstack11ll1l_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨ↯"))
            bstack1l1l111ll_opy_.bstack1lllll111l1l_opy_(commands)
            bstack1lllll111ll1_opy_ = capabilities.get(bstack11ll1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ↰"))
            bstack1l1l111ll_opy_.bstack1lllll11l111_opy_(bstack1lllll111ll1_opy_)
            bstack1l1l111ll_opy_.store()
        return [bstack1llll11l11ll_opy_, bstack11ll1ll11_opy_[bstack11ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ↱")]]
    @classmethod
    def bstack1llll11l1l1l_opy_(cls, response=None):
        os.environ[bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ↲")] = bstack11ll1l_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ↳")
        os.environ[bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ↴")] = bstack11ll1l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ↵")
        os.environ[bstack11ll1l_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡆࡓࡒࡖࡌࡆࡖࡈࡈࠬ↶")] = bstack11ll1l_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭↷")
        os.environ[bstack11ll1l_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧ↸")] = bstack11ll1l_opy_ (u"ࠤࡱࡹࡱࡲࠢ↹")
        os.environ[bstack11ll1l_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫ↺")] = bstack11ll1l_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ↻")
        cls.bstack1llll11lll1l_opy_(response, bstack11ll1l_opy_ (u"ࠧࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠧ↼"))
        return [None, None, None]
    @classmethod
    def bstack1llll11lll11_opy_(cls, response=None):
        os.environ[bstack11ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ↽")] = bstack11ll1l_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬ↾")
        os.environ[bstack11ll1l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭↿")] = bstack11ll1l_opy_ (u"ࠩࡱࡹࡱࡲࠧ⇀")
        os.environ[bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ⇁")] = bstack11ll1l_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ⇂")
        cls.bstack1llll11lll1l_opy_(response, bstack11ll1l_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠧ⇃"))
        return [None, None, None]
    @classmethod
    def bstack1llll11ll1l1_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack11ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ⇄")] = jwt
        os.environ[bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ⇅")] = build_hashed_id
    @classmethod
    def bstack1llll11lll1l_opy_(cls, response=None, product=bstack11ll1l_opy_ (u"ࠣࠤ⇆")):
        if response == None or response.get(bstack11ll1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࡴࠩ⇇")) == None:
            logger.error(product + bstack11ll1l_opy_ (u"ࠥࠤࡇࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠧ⇈"))
            return
        for error in response[bstack11ll1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࡶࠫ⇉")]:
            bstack111l1l11l11_opy_ = error[bstack11ll1l_opy_ (u"ࠬࡱࡥࡺࠩ⇊")]
            error_message = error[bstack11ll1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⇋")]
            if error_message:
                if bstack111l1l11l11_opy_ == bstack11ll1l_opy_ (u"ࠢࡆࡔࡕࡓࡗࡥࡁࡄࡅࡈࡗࡘࡥࡄࡆࡐࡌࡉࡉࠨ⇌"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack11ll1l_opy_ (u"ࠣࡆࡤࡸࡦࠦࡵࡱ࡮ࡲࡥࡩࠦࡴࡰࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࠤ⇍") + product + bstack11ll1l_opy_ (u"ࠤࠣࡪࡦ࡯࡬ࡦࡦࠣࡨࡺ࡫ࠠࡵࡱࠣࡷࡴࡳࡥࠡࡧࡵࡶࡴࡸࠢ⇎"))
    @classmethod
    def bstack1llll11ll111_opy_(cls):
        if cls.bstack11l111lll11_opy_ is not None:
            return
        cls.bstack11l111lll11_opy_ = bstack111l1lll111_opy_(cls.post_data)
        cls.bstack11l111lll11_opy_.start()
    @classmethod
    def bstack1l1l1l1l_opy_(cls):
        if cls.bstack11l111lll11_opy_ is None:
            return
        cls.bstack11l111lll11_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1l111lll_opy_, event_url=bstack11ll1l_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡦࡺࡣࡩࠩ⇏")):
        config = {
            bstack11ll1l_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ⇐"): cls.default_headers()
        }
        logger.debug(bstack11ll1l_opy_ (u"ࠧࡶ࡯ࡴࡶࡢࡨࡦࡺࡡ࠻ࠢࡖࡩࡳࡪࡩ࡯ࡩࠣࡨࡦࡺࡡࠡࡶࡲࠤࡹ࡫ࡳࡵࡪࡸࡦࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴࡴࠢࡾࢁࠧ⇑").format(bstack11ll1l_opy_ (u"࠭ࠬࠡࠩ⇒").join([event[bstack11ll1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ⇓")] for event in bstack1l111lll_opy_])))
        response = bstack1l1llllll_opy_(bstack11ll1l_opy_ (u"ࠨࡒࡒࡗ࡙࠭⇔"), cls.request_url(event_url), bstack1l111lll_opy_, config)
        bstack1llll1llll1l_opy_ = response.json()
    @classmethod
    def bstack1lll1111_opy_(cls, bstack1l111lll_opy_, event_url=bstack11ll1l_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨ⇕")):
        logger.debug(bstack11ll1l_opy_ (u"ࠥࡷࡪࡴࡤࡠࡦࡤࡸࡦࡀࠠࡂࡶࡷࡩࡲࡶࡴࡪࡰࡪࠤࡹࡵࠠࡢࡦࡧࠤࡩࡧࡴࡢࠢࡷࡳࠥࡨࡡࡵࡥ࡫ࠤࡼ࡯ࡴࡩࠢࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪࡀࠠࡼࡿࠥ⇖").format(bstack1l111lll_opy_[bstack11ll1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ⇗")]))
        if not bstack1llll11l1l_opy_.bstack1llll1l11111_opy_(bstack1l111lll_opy_[bstack11ll1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ⇘")]):
            logger.debug(bstack11ll1l_opy_ (u"ࠨࡳࡦࡰࡧࡣࡩࡧࡴࡢ࠼ࠣࡒࡴࡺࠠࡢࡦࡧ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫࠺ࠡࡽࢀࠦ⇙").format(bstack1l111lll_opy_[bstack11ll1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ⇚")]))
            return
        bstack11111ll1ll_opy_ = bstack1llll11l1l_opy_.bstack1llll111lll1_opy_(bstack1l111lll_opy_[bstack11ll1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ⇛")], bstack1l111lll_opy_.get(bstack11ll1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ⇜")))
        if bstack11111ll1ll_opy_ != None:
            if bstack1l111lll_opy_.get(bstack11ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬ⇝")) != None:
                bstack1l111lll_opy_[bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭⇞")][bstack11ll1l_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪ⇟")] = bstack11111ll1ll_opy_
            else:
                bstack1l111lll_opy_[bstack11ll1l_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫ⇠")] = bstack11111ll1ll_opy_
        if event_url == bstack11ll1l_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡣࡷࡧ࡭࠭⇡"):
            cls.bstack1llll11ll111_opy_()
            logger.debug(bstack11ll1l_opy_ (u"ࠣࡵࡨࡲࡩࡥࡤࡢࡶࡤ࠾ࠥࡇࡤࡥ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡸࡴࠦࡢࡢࡶࡦ࡬ࠥࡽࡩࡵࡪࠣࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫࠺ࠡࡽࢀࠦ⇢").format(bstack1l111lll_opy_[bstack11ll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭⇣")]))
            cls.bstack11l111lll11_opy_.add(bstack1l111lll_opy_)
        elif event_url == bstack11ll1l_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨ⇤"):
            cls.post_data([bstack1l111lll_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1lll1ll1_opy_(cls, logs):
        for log in logs:
            bstack1llll11lllll_opy_ = {
                bstack11ll1l_opy_ (u"ࠫࡰ࡯࡮ࡥࠩ⇥"): bstack11ll1l_opy_ (u"࡚ࠬࡅࡔࡖࡢࡐࡔࡍࠧ⇦"),
                bstack11ll1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ⇧"): log[bstack11ll1l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭⇨")],
                bstack11ll1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ⇩"): log[bstack11ll1l_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ⇪")],
                bstack11ll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡠࡴࡨࡷࡵࡵ࡮ࡴࡧࠪ⇫"): {},
                bstack11ll1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⇬"): log[bstack11ll1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭⇭")],
            }
            if bstack11ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇮") in log:
                bstack1llll11lllll_opy_[bstack11ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇯")] = log[bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇰")]
            elif bstack11ll1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇱") in log:
                bstack1llll11lllll_opy_[bstack11ll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇲")] = log[bstack11ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇳")]
            cls.bstack1lll1111_opy_({
                bstack11ll1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ⇴"): bstack11ll1l_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ⇵"),
                bstack11ll1l_opy_ (u"ࠧ࡭ࡱࡪࡷࠬ⇶"): [bstack1llll11lllll_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll11ll11l_opy_(cls, steps):
        bstack1llll11l111l_opy_ = []
        for step in steps:
            bstack1llll11l11l1_opy_ = {
                bstack11ll1l_opy_ (u"ࠨ࡭࡬ࡲࡩ࠭⇷"): bstack11ll1l_opy_ (u"ࠩࡗࡉࡘ࡚࡟ࡔࡖࡈࡔࠬ⇸"),
                bstack11ll1l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ⇹"): step[bstack11ll1l_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ⇺")],
                bstack11ll1l_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ⇻"): step[bstack11ll1l_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ⇼")],
                bstack11ll1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⇽"): step[bstack11ll1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⇾")],
                bstack11ll1l_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫ⇿"): step[bstack11ll1l_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬ∀")]
            }
            if bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ∁") in step:
                bstack1llll11l11l1_opy_[bstack11ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ∂")] = step[bstack11ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭∃")]
            elif bstack11ll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ∄") in step:
                bstack1llll11l11l1_opy_[bstack11ll1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ∅")] = step[bstack11ll1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ∆")]
            bstack1llll11l111l_opy_.append(bstack1llll11l11l1_opy_)
        cls.bstack1lll1111_opy_({
            bstack11ll1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ∇"): bstack11ll1l_opy_ (u"ࠫࡑࡵࡧࡄࡴࡨࡥࡹ࡫ࡤࠨ∈"),
            bstack11ll1l_opy_ (u"ࠬࡲ࡯ࡨࡵࠪ∉"): bstack1llll11l111l_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack111l11l1ll_opy_, stage=STAGE.bstack11ll11lll_opy_)
    def bstack111l11lll1_opy_(cls, screenshot):
        cls.bstack1lll1111_opy_({
            bstack11ll1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ∊"): bstack11ll1l_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫ∋"),
            bstack11ll1l_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭∌"): [{
                bstack11ll1l_opy_ (u"ࠩ࡮࡭ࡳࡪࠧ∍"): bstack11ll1l_opy_ (u"ࠪࡘࡊ࡙ࡔࡠࡕࡆࡖࡊࡋࡎࡔࡊࡒࡘࠬ∎"),
                bstack11ll1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ∏"): datetime.datetime.utcnow().isoformat() + bstack11ll1l_opy_ (u"ࠬࡠࠧ∐"),
                bstack11ll1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ∑"): screenshot[bstack11ll1l_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭−")],
                bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ∓"): screenshot[bstack11ll1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ∔")]
            }]
        }, event_url=bstack11ll1l_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨ∕"))
    @classmethod
    @error_handler(class_method=True)
    def bstack11ll11l11l_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1lll1111_opy_({
            bstack11ll1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ∖"): bstack11ll1l_opy_ (u"ࠬࡉࡂࡕࡕࡨࡷࡸ࡯࡯࡯ࡅࡵࡩࡦࡺࡥࡥࠩ∗"),
            bstack11ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨ∘"): {
                bstack11ll1l_opy_ (u"ࠢࡶࡷ࡬ࡨࠧ∙"): cls.current_test_uuid(),
                bstack11ll1l_opy_ (u"ࠣ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠢ√"): cls.bstack1l11llll_opy_(driver)
            }
        })
    @classmethod
    def bstack1ll111ll_opy_(cls, event: str, bstack1l111lll_opy_: bstack1ll1ll11_opy_):
        bstack1l11ll11_opy_ = {
            bstack11ll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭∛"): event,
            bstack1l111lll_opy_.event_key(): bstack1l111lll_opy_.bstack11llllll_opy_(event)
        }
        cls.bstack1lll1111_opy_(bstack1l11ll11_opy_)
        result = getattr(bstack1l111lll_opy_, bstack11ll1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ∜"), None)
        if event == bstack11ll1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ∝"):
            threading.current_thread().bstackTestMeta = {bstack11ll1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ∞"): bstack11ll1l_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ∟")}
        elif event == bstack11ll1l_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ∠"):
            threading.current_thread().bstackTestMeta = {bstack11ll1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ∡"): getattr(result, bstack11ll1l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ∢"), bstack11ll1l_opy_ (u"ࠪࠫ∣"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ∤"), None) is None or os.environ[bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ∥")] == bstack11ll1l_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ∦")) and (os.environ.get(bstack11ll1l_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ∧"), None) is None or os.environ[bstack11ll1l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭∨")] == bstack11ll1l_opy_ (u"ࠤࡱࡹࡱࡲࠢ∩")):
            return False
        return True
    @staticmethod
    def bstack1llll11l1lll_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1l1l1lll_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack11ll1l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ∪"): bstack11ll1l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ∫"),
            bstack11ll1l_opy_ (u"ࠬ࡞࠭ࡃࡕࡗࡅࡈࡑ࠭ࡕࡇࡖࡘࡔࡖࡓࠨ∬"): bstack11ll1l_opy_ (u"࠭ࡴࡳࡷࡨࠫ∭")
        }
        if os.environ.get(bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ∮"), None):
            headers[bstack11ll1l_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨ∯")] = bstack11ll1l_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬ∰").format(os.environ[bstack11ll1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠢ∱")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack11ll1l_opy_ (u"ࠫࢀࢃ࠯ࡼࡿࠪ∲").format(bstack1llll1l1111l_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack11ll1l_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ∳"), None)
    @staticmethod
    def bstack1l11llll_opy_(driver):
        return {
            bstack1111lll1ll1_opy_(): bstack111l1ll1ll1_opy_(driver)
        }
    @staticmethod
    def bstack1llll1l111l1_opy_(exception_info, report):
        return [{bstack11ll1l_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩ∴"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11111111ll_opy_(typename):
        if bstack11ll1l_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࠥ∵") in typename:
            return bstack11ll1l_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࡉࡷࡸ࡯ࡳࠤ∶")
        return bstack11ll1l_opy_ (u"ࠤࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠥ∷")