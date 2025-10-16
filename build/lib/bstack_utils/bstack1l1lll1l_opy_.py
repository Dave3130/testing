# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import json
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111l111lll1_opy_, bstack111l1l1l111_opy_, bstack1ll1llll11_opy_, error_handler, bstack111l1ll1l11_opy_, bstack1111lll11ll_opy_, bstack1111ll111ll_opy_, bstack1ll11l1l_opy_, bstack1llll11l_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l11l1llll_opy_ import bstack111ll11l1ll_opy_
import bstack_utils.bstack1l1l11ll11_opy_ as bstack11l11ll111_opy_
from bstack_utils.bstack1ll111l1_opy_ import bstack11lll1l1_opy_
import bstack_utils.accessibility as bstack11111ll1_opy_
from bstack_utils.bstack1ll1l1llll_opy_ import bstack1ll1l1llll_opy_
from bstack_utils.bstack1lll1111_opy_ import bstack1l1111l1_opy_
from bstack_utils.constants import bstack1ll1lll111_opy_
bstack1llll1l11ll1_opy_ = bstack1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡣࡰ࡮࡯ࡩࡨࡺ࡯ࡳ࠯ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ⃿")
logger = logging.getLogger(__name__)
class bstack1ll1lll1_opy_:
    bstack11l11l1llll_opy_ = None
    bs_config = None
    bstack11ll1l1ll1_opy_ = None
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack11l1l1l11l1_opy_, stage=STAGE.bstack11ll111111_opy_)
    def launch(cls, bs_config, bstack11ll1l1ll1_opy_):
        cls.bs_config = bs_config
        cls.bstack11ll1l1ll1_opy_ = bstack11ll1l1ll1_opy_
        try:
            cls.bstack1llll1ll111l_opy_()
            bstack1llll1ll1l11_opy_ = bstack111l111lll1_opy_(bs_config)
            bstack1llll1ll1ll1_opy_ = bstack111l1l1l111_opy_(bs_config)
            data = bstack11l11ll111_opy_.bstack1llll1l11l1l_opy_(bs_config, bstack11ll1l1ll1_opy_)
            config = {
                bstack1l_opy_ (u"࠭ࡡࡶࡶ࡫ࠫ℀"): (bstack1llll1ll1l11_opy_, bstack1llll1ll1ll1_opy_),
                bstack1l_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨ℁"): cls.default_headers()
            }
            response = bstack1ll1llll11_opy_(bstack1l_opy_ (u"ࠨࡒࡒࡗ࡙࠭ℂ"), cls.request_url(bstack1l_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠳࠱ࡥࡹ࡮ࡲࡤࡴࠩ℃")), data, config)
            if response.status_code != 200:
                bstack111llllll_opy_ = response.json()
                if bstack111llllll_opy_[bstack1l_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ℄")] == False:
                    cls.bstack1llll1l1111l_opy_(bstack111llllll_opy_)
                    return
                cls.bstack1llll1l1l11l_opy_(bstack111llllll_opy_[bstack1l_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ℅")])
                cls.bstack1llll11lll11_opy_(bstack111llllll_opy_[bstack1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ℆")])
                return None
            bstack1llll1l111ll_opy_ = cls.bstack1llll1l1l1l1_opy_(response)
            return bstack1llll1l111ll_opy_, response.json()
        except Exception as error:
            logger.error(bstack1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡦࡺ࡯࡬ࡥࠢࡩࡳࡷࠦࡔࡦࡵࡷࡌࡺࡨ࠺ࠡࡽࢀࠦℇ").format(str(error)))
            return None
    @classmethod
    @error_handler(class_method=True)
    def stop(cls, bstack1llll11llll1_opy_=None):
        if not bstack11lll1l1_opy_.on() and not bstack11111ll1_opy_.on():
            return
        if os.environ.get(bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ℈")) == bstack1l_opy_ (u"ࠣࡰࡸࡰࡱࠨ℉") or os.environ.get(bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧℊ")) == bstack1l_opy_ (u"ࠥࡲࡺࡲ࡬ࠣℋ"):
            logger.error(bstack1l_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡵࡰࠡࡤࡸ࡭ࡱࡪࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤ࡙࡫ࡳࡵࡊࡸࡦ࠿ࠦࡍࡪࡵࡶ࡭ࡳ࡭ࠠࡢࡷࡷ࡬ࡪࡴࡴࡪࡥࡤࡸ࡮ࡵ࡮ࠡࡶࡲ࡯ࡪࡴࠧℌ"))
            return {
                bstack1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬℍ"): bstack1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬℎ"),
                bstack1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨℏ"): bstack1l_opy_ (u"ࠨࡖࡲ࡯ࡪࡴ࠯ࡣࡷ࡬ࡰࡩࡏࡄࠡ࡫ࡶࠤࡺࡴࡤࡦࡨ࡬ࡲࡪࡪࠬࠡࡤࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡰ࡭࡬࡮ࡴࠡࡪࡤࡺࡪࠦࡦࡢ࡫࡯ࡩࡩ࠭ℐ")
            }
        try:
            cls.bstack11l11l1llll_opy_.shutdown()
            data = {
                bstack1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧℑ"): bstack1ll11l1l_opy_()
            }
            if not bstack1llll11llll1_opy_ is None:
                data[bstack1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡳࡥࡵࡣࡧࡥࡹࡧࠧℒ")] = [{
                    bstack1l_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫℓ"): bstack1l_opy_ (u"ࠬࡻࡳࡦࡴࡢ࡯࡮ࡲ࡬ࡦࡦࠪ℔"),
                    bstack1l_opy_ (u"࠭ࡳࡪࡩࡱࡥࡱ࠭ℕ"): bstack1llll11llll1_opy_
                }]
            config = {
                bstack1l_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨ№"): cls.default_headers()
            }
            bstack11ll11ll111_opy_ = bstack1l_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀ࠳ࡸࡺ࡯ࡱࠩ℗").format(os.environ[bstack1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠢ℘")])
            bstack1llll1ll1111_opy_ = cls.request_url(bstack11ll11ll111_opy_)
            response = bstack1ll1llll11_opy_(bstack1l_opy_ (u"ࠪࡔ࡚࡚ࠧℙ"), bstack1llll1ll1111_opy_, data, config)
            if not response.ok:
                raise Exception(bstack1l_opy_ (u"ࠦࡘࡺ࡯ࡱࠢࡵࡩࡶࡻࡥࡴࡶࠣࡲࡴࡺࠠࡰ࡭ࠥℚ"))
        except Exception as error:
            logger.error(bstack1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸࡺ࡯ࡱࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡷࡳ࡚ࠥࡥࡴࡶࡋࡹࡧࡀ࠺ࠡࠤℛ") + str(error))
            return {
                bstack1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ℜ"): bstack1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ℝ"),
                bstack1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ℞"): str(error)
            }
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll1l1l1l1_opy_(cls, response):
        bstack111llllll_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1llll1l111ll_opy_ = {}
        if bstack111llllll_opy_.get(bstack1l_opy_ (u"ࠩ࡭ࡻࡹ࠭℟")) is None:
            os.environ[bstack1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ℠")] = bstack1l_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ℡")
        else:
            os.environ[bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ™")] = bstack111llllll_opy_.get(bstack1l_opy_ (u"࠭ࡪࡸࡶࠪ℣"), bstack1l_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬℤ"))
        os.environ[bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭℥")] = bstack111llllll_opy_.get(bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫΩ"), bstack1l_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ℧"))
        logger.info(bstack1l_opy_ (u"࡙ࠫ࡫ࡳࡵࡪࡸࡦࠥࡹࡴࡢࡴࡷࡩࡩࠦࡷࡪࡶ࡫ࠤ࡮ࡪ࠺ࠡࠩℨ") + os.getenv(bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ℩")));
        if bstack11lll1l1_opy_.bstack11l11l1ll11_opy_(cls.bs_config, cls.bstack11ll1l1ll1_opy_.get(bstack1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡸࡷࡪࡪࠧK"), bstack1l_opy_ (u"ࠧࠨÅ"))) is True:
            bstack11ll11l1lll_opy_, build_hashed_id, bstack1llll1l11111_opy_ = cls.bstack1llll1l1ll11_opy_(bstack111llllll_opy_)
            if bstack11ll11l1lll_opy_ != None and build_hashed_id != None:
                bstack1llll1l111ll_opy_[bstack1l_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨℬ")] = {
                    bstack1l_opy_ (u"ࠩ࡭ࡻࡹࡥࡴࡰ࡭ࡨࡲࠬℭ"): bstack11ll11l1lll_opy_,
                    bstack1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ℮"): build_hashed_id,
                    bstack1l_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨℯ"): bstack1llll1l11111_opy_
                }
            else:
                bstack1llll1l111ll_opy_[bstack1l_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬℰ")] = {}
        else:
            bstack1llll1l111ll_opy_[bstack1l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ℱ")] = {}
        bstack1llll1l111l1_opy_, build_hashed_id = cls.bstack1llll1l1ll1l_opy_(bstack111llllll_opy_)
        if bstack1llll1l111l1_opy_ != None and build_hashed_id != None:
            bstack1llll1l111ll_opy_[bstack1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧℲ")] = {
                bstack1l_opy_ (u"ࠨࡣࡸࡸ࡭ࡥࡴࡰ࡭ࡨࡲࠬℳ"): bstack1llll1l111l1_opy_,
                bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫℴ"): build_hashed_id,
            }
        else:
            bstack1llll1l111ll_opy_[bstack1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪℵ")] = {}
        if bstack1llll1l111ll_opy_[bstack1l_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫℶ")].get(bstack1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧℷ")) != None or bstack1llll1l111ll_opy_[bstack1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ℸ")].get(bstack1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩℹ")) != None:
            cls.bstack1llll1ll11l1_opy_(bstack111llllll_opy_.get(bstack1l_opy_ (u"ࠨ࡬ࡺࡸࠬ℺")), bstack111llllll_opy_.get(bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ℻")))
        return bstack1llll1l111ll_opy_
    @classmethod
    def bstack1llll1l1ll11_opy_(cls, bstack111llllll_opy_):
        if bstack111llllll_opy_.get(bstack1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪℼ")) == None:
            cls.bstack1llll1l1l11l_opy_()
            return [None, None, None]
        if bstack111llllll_opy_[bstack1l_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫℽ")][bstack1l_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭ℾ")] != True:
            cls.bstack1llll1l1l11l_opy_(bstack111llllll_opy_[bstack1l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭ℿ")])
            return [None, None, None]
        logger.debug(bstack1l_opy_ (u"ࠧࡼࡿࠣࡆࡺ࡯࡬ࡥࠢࡦࡶࡪࡧࡴࡪࡱࡱࠤࡘࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬ࠢࠩ⅀").format(bstack1ll1lll111_opy_))
        os.environ[bstack1l_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡈࡕࡍࡑࡎࡈࡘࡊࡊࠧ⅁")] = bstack1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ⅂")
        if bstack111llllll_opy_.get(bstack1l_opy_ (u"ࠪ࡮ࡼࡺࠧ⅃")):
            os.environ[bstack1l_opy_ (u"ࠫࡈࡘࡅࡅࡇࡑࡘࡎࡇࡌࡔࡡࡉࡓࡗࡥࡃࡓࡃࡖࡌࡤࡘࡅࡑࡑࡕࡘࡎࡔࡇࠨ⅄")] = json.dumps({
                bstack1l_opy_ (u"ࠬࡻࡳࡦࡴࡱࡥࡲ࡫ࠧⅅ"): bstack111l111lll1_opy_(cls.bs_config),
                bstack1l_opy_ (u"࠭ࡰࡢࡵࡶࡻࡴࡸࡤࠨⅆ"): bstack111l1l1l111_opy_(cls.bs_config)
            })
        if bstack111llllll_opy_.get(bstack1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩⅇ")):
            os.environ[bstack1l_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧⅈ")] = bstack111llllll_opy_[bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫⅉ")]
        if bstack111llllll_opy_[bstack1l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ⅊")].get(bstack1l_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ⅋"), {}).get(bstack1l_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩ⅌")):
            os.environ[bstack1l_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧ⅍")] = str(bstack111llllll_opy_[bstack1l_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧⅎ")][bstack1l_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩ⅏")][bstack1l_opy_ (u"ࠩࡤࡰࡱࡵࡷࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭⅐")])
        else:
            os.environ[bstack1l_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫ⅑")] = bstack1l_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ⅒")
        return [bstack111llllll_opy_[bstack1l_opy_ (u"ࠬࡰࡷࡵࠩ⅓")], bstack111llllll_opy_[bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ⅔")], os.environ[bstack1l_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡆࡒࡌࡐ࡙ࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࡓࠨ⅕")]]
    @classmethod
    def bstack1llll1l1ll1l_opy_(cls, bstack111llllll_opy_):
        if bstack111llllll_opy_.get(bstack1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⅖")) == None:
            cls.bstack1llll11lll11_opy_()
            return [None, None]
        if bstack111llllll_opy_[bstack1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⅗")][bstack1l_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ⅘")] != True:
            cls.bstack1llll11lll11_opy_(bstack111llllll_opy_[bstack1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⅙")])
            return [None, None]
        if bstack111llllll_opy_[bstack1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⅚")].get(bstack1l_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ⅛")):
            logger.debug(bstack1l_opy_ (u"ࠧࡕࡧࡶࡸࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠤࠫ⅜"))
            parsed = json.loads(os.getenv(bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ⅝"), bstack1l_opy_ (u"ࠩࡾࢁࠬ⅞")))
            capabilities = bstack11l11ll111_opy_.bstack1llll11lll1l_opy_(bstack111llllll_opy_[bstack1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⅟")][bstack1l_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬⅠ")][bstack1l_opy_ (u"ࠬࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫⅡ")], bstack1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫⅢ"), bstack1l_opy_ (u"ࠧࡷࡣ࡯ࡹࡪ࠭Ⅳ"))
            bstack1llll1l111l1_opy_ = capabilities[bstack1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡕࡱ࡮ࡩࡳ࠭Ⅴ")]
            os.environ[bstack1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧⅥ")] = bstack1llll1l111l1_opy_
            if bstack1l_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷࡩࠧⅦ") in bstack111llllll_opy_ and bstack111llllll_opy_.get(bstack1l_opy_ (u"ࠦࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠥⅧ")) is None:
                parsed[bstack1l_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭Ⅸ")] = capabilities[bstack1l_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧⅩ")]
            os.environ[bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨⅪ")] = json.dumps(parsed)
            scripts = bstack11l11ll111_opy_.bstack1llll11lll1l_opy_(bstack111llllll_opy_[bstack1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨⅫ")][bstack1l_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪⅬ")][bstack1l_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫⅭ")], bstack1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩⅮ"), bstack1l_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩ࠭Ⅿ"))
            bstack1ll1l1llll_opy_.bstack1l11l1llll_opy_(scripts)
            commands = bstack111llllll_opy_[bstack1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ⅰ")][bstack1l_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨⅱ")][bstack1l_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࡗࡳ࡜ࡸࡡࡱࠩⅲ")].get(bstack1l_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶࠫⅳ"))
            bstack1ll1l1llll_opy_.bstack1lllll1l1l1l_opy_(commands)
            bstack1lllll1l11l1_opy_ = capabilities.get(bstack1l_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨⅴ"))
            bstack1ll1l1llll_opy_.bstack1lllll1l1lll_opy_(bstack1lllll1l11l1_opy_)
            bstack1ll1l1llll_opy_.store()
        return [bstack1llll1l111l1_opy_, bstack111llllll_opy_[bstack1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ⅵ")]]
    @classmethod
    def bstack1llll1l1l11l_opy_(cls, response=None):
        os.environ[bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪⅶ")] = bstack1l_opy_ (u"࠭࡮ࡶ࡮࡯ࠫⅷ")
        os.environ[bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫⅸ")] = bstack1l_opy_ (u"ࠨࡰࡸࡰࡱ࠭ⅹ")
        os.environ[bstack1l_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡉࡏࡎࡒࡏࡉ࡙ࡋࡄࠨⅺ")] = bstack1l_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩⅻ")
        os.environ[bstack1l_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪⅼ")] = bstack1l_opy_ (u"ࠧࡴࡵ࡭࡮ࠥⅽ")
        os.environ[bstack1l_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧⅾ")] = bstack1l_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧⅿ")
        cls.bstack1llll1l1111l_opy_(response, bstack1l_opy_ (u"ࠣࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠣↀ"))
        return [None, None, None]
    @classmethod
    def bstack1llll11lll11_opy_(cls, response=None):
        os.environ[bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧↁ")] = bstack1l_opy_ (u"ࠪࡲࡺࡲ࡬ࠨↂ")
        os.environ[bstack1l_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩↃ")] = bstack1l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪↄ")
        os.environ[bstack1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪↅ")] = bstack1l_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬↆ")
        cls.bstack1llll1l1111l_opy_(response, bstack1l_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠣↇ"))
        return [None, None, None]
    @classmethod
    def bstack1llll1ll11l1_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ↈ")] = jwt
        os.environ[bstack1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ↉")] = build_hashed_id
    @classmethod
    def bstack1llll1l1111l_opy_(cls, response=None, product=bstack1l_opy_ (u"ࠦࠧ↊")):
        if response == None or response.get(bstack1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷࠬ↋")) == None:
            logger.error(product + bstack1l_opy_ (u"ࠨࠠࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤࠣ↌"))
            return
        for error in response[bstack1l_opy_ (u"ࠧࡦࡴࡵࡳࡷࡹࠧ↍")]:
            bstack111l1lllll1_opy_ = error[bstack1l_opy_ (u"ࠨ࡭ࡨࡽࠬ↎")]
            error_message = error[bstack1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ↏")]
            if error_message:
                if bstack111l1lllll1_opy_ == bstack1l_opy_ (u"ࠥࡉࡗࡘࡏࡓࡡࡄࡇࡈࡋࡓࡔࡡࡇࡉࡓࡏࡅࡅࠤ←"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack1l_opy_ (u"ࠦࡉࡧࡴࡢࠢࡸࡴࡱࡵࡡࡥࠢࡷࡳࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࠧ↑") + product + bstack1l_opy_ (u"ࠧࠦࡦࡢ࡫࡯ࡩࡩࠦࡤࡶࡧࠣࡸࡴࠦࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠥ→"))
    @classmethod
    def bstack1llll1ll111l_opy_(cls):
        if cls.bstack11l11l1llll_opy_ is not None:
            return
        cls.bstack11l11l1llll_opy_ = bstack111ll11l1ll_opy_(cls.post_data)
        cls.bstack11l11l1llll_opy_.start()
    @classmethod
    def bstack11llll1l_opy_(cls):
        if cls.bstack11l11l1llll_opy_ is None:
            return
        cls.bstack11l11l1llll_opy_.shutdown()
    @classmethod
    @error_handler(class_method=True)
    def post_data(cls, bstack1l111lll_opy_, event_url=bstack1l_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡢࡶࡦ࡬ࠬ↓")):
        config = {
            bstack1l_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨ↔"): cls.default_headers()
        }
        logger.debug(bstack1l_opy_ (u"ࠣࡲࡲࡷࡹࡥࡤࡢࡶࡤ࠾࡙ࠥࡥ࡯ࡦ࡬ࡲ࡬ࠦࡤࡢࡶࡤࠤࡹࡵࠠࡵࡧࡶࡸ࡭ࡻࡢࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷࡷࠥࢁࡽࠣ↕").format(bstack1l_opy_ (u"ࠩ࠯ࠤࠬ↖").join([event[bstack1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ↗")] for event in bstack1l111lll_opy_])))
        response = bstack1ll1llll11_opy_(bstack1l_opy_ (u"ࠫࡕࡕࡓࡕࠩ↘"), cls.request_url(event_url), bstack1l111lll_opy_, config)
        bstack1lllll1111l1_opy_ = response.json()
    @classmethod
    def bstack1lll11ll_opy_(cls, bstack1l111lll_opy_, event_url=bstack1l_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡡࡵࡥ࡫ࠫ↙")):
        logger.debug(bstack1l_opy_ (u"ࠨࡳࡦࡰࡧࡣࡩࡧࡴࡢ࠼ࠣࡅࡹࡺࡥ࡮ࡲࡷ࡭ࡳ࡭ࠠࡵࡱࠣࡥࡩࡪࠠࡥࡣࡷࡥࠥࡺ࡯ࠡࡤࡤࡸࡨ࡮ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨ↚").format(bstack1l111lll_opy_[bstack1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ↛")]))
        if not bstack11l11ll111_opy_.bstack1llll11ll1ll_opy_(bstack1l111lll_opy_[bstack1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ↜")]):
            logger.debug(bstack1l_opy_ (u"ࠤࡶࡩࡳࡪ࡟ࡥࡣࡷࡥ࠿ࠦࡎࡰࡶࠣࡥࡩࡪࡩ࡯ࡩࠣࡨࡦࡺࡡࠡࡹ࡬ࡸ࡭ࠦࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧ࠽ࠤࢀࢃࠢ↝").format(bstack1l111lll_opy_[bstack1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ↞")]))
            return
        bstack1111llll11_opy_ = bstack11l11ll111_opy_.bstack1llll1l1l111_opy_(bstack1l111lll_opy_[bstack1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ↟")], bstack1l111lll_opy_.get(bstack1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧ↠")))
        if bstack1111llll11_opy_ != None:
            if bstack1l111lll_opy_.get(bstack1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨ↡")) != None:
                bstack1l111lll_opy_[bstack1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩ↢")][bstack1l_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭↣")] = bstack1111llll11_opy_
            else:
                bstack1l111lll_opy_[bstack1l_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࡢࡱࡦࡶࠧ↤")] = bstack1111llll11_opy_
        if event_url == bstack1l_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡦࡺࡣࡩࠩ↥"):
            cls.bstack1llll1ll111l_opy_()
            logger.debug(bstack1l_opy_ (u"ࠦࡸ࡫࡮ࡥࡡࡧࡥࡹࡧ࠺ࠡࡃࡧࡨ࡮ࡴࡧࠡࡦࡤࡸࡦࠦࡴࡰࠢࡥࡥࡹࡩࡨࠡࡹ࡬ࡸ࡭ࠦࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧ࠽ࠤࢀࢃࠢ↦").format(bstack1l111lll_opy_[bstack1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ↧")]))
            cls.bstack11l11l1llll_opy_.add(bstack1l111lll_opy_)
        elif event_url == bstack1l_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫ↨"):
            cls.post_data([bstack1l111lll_opy_], event_url)
    @classmethod
    @error_handler(class_method=True)
    def bstack1l1l1l11_opy_(cls, logs):
        for log in logs:
            bstack1llll1l1llll_opy_ = {
                bstack1l_opy_ (u"ࠧ࡬࡫ࡱࡨࠬ↩"): bstack1l_opy_ (u"ࠨࡖࡈࡗ࡙ࡥࡌࡐࡉࠪ↪"),
                bstack1l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ↫"): log[bstack1l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ↬")],
                bstack1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ↭"): log[bstack1l_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ↮")],
                bstack1l_opy_ (u"࠭ࡨࡵࡶࡳࡣࡷ࡫ࡳࡱࡱࡱࡷࡪ࠭↯"): {},
                bstack1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ↰"): log[bstack1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ↱")],
            }
            if bstack1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ↲") in log:
                bstack1llll1l1llll_opy_[bstack1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ↳")] = log[bstack1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ↴")]
            elif bstack1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ↵") in log:
                bstack1llll1l1llll_opy_[bstack1l_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭↶")] = log[bstack1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ↷")]
            cls.bstack1lll11ll_opy_({
                bstack1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ↸"): bstack1l_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭↹"),
                bstack1l_opy_ (u"ࠪࡰࡴ࡭ࡳࠨ↺"): [bstack1llll1l1llll_opy_]
            })
    @classmethod
    @error_handler(class_method=True)
    def bstack1llll1l11lll_opy_(cls, steps):
        bstack1llll1l1l1ll_opy_ = []
        for step in steps:
            bstack1llll1l1lll1_opy_ = {
                bstack1l_opy_ (u"ࠫࡰ࡯࡮ࡥࠩ↻"): bstack1l_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗ࡙ࡋࡐࠨ↼"),
                bstack1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ↽"): step[bstack1l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭↾")],
                bstack1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ↿"): step[bstack1l_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ⇀")],
                bstack1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⇁"): step[bstack1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⇂")],
                bstack1l_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧ⇃"): step[bstack1l_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨ⇄")]
            }
            if bstack1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇅") in step:
                bstack1llll1l1lll1_opy_[bstack1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇆")] = step[bstack1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ⇇")]
            elif bstack1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇈") in step:
                bstack1llll1l1lll1_opy_[bstack1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇉")] = step[bstack1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⇊")]
            bstack1llll1l1l1ll_opy_.append(bstack1llll1l1lll1_opy_)
        cls.bstack1lll11ll_opy_({
            bstack1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⇋"): bstack1l_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫ⇌"),
            bstack1l_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭⇍"): bstack1llll1l1l1ll_opy_
        })
    @classmethod
    @error_handler(class_method=True)
    @measure(event_name=EVENTS.bstack1l1l11l1ll_opy_, stage=STAGE.bstack11ll111111_opy_)
    def bstack1l11ll11l1_opy_(cls, screenshot):
        cls.bstack1lll11ll_opy_({
            bstack1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭⇎"): bstack1l_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧ⇏"),
            bstack1l_opy_ (u"ࠫࡱࡵࡧࡴࠩ⇐"): [{
                bstack1l_opy_ (u"ࠬࡱࡩ࡯ࡦࠪ⇑"): bstack1l_opy_ (u"࠭ࡔࡆࡕࡗࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࠨ⇒"),
                bstack1l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ⇓"): datetime.datetime.utcnow().isoformat() + bstack1l_opy_ (u"ࠨ࡜ࠪ⇔"),
                bstack1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⇕"): screenshot[bstack1l_opy_ (u"ࠪ࡭ࡲࡧࡧࡦࠩ⇖")],
                bstack1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇗"): screenshot[bstack1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⇘")]
            }]
        }, event_url=bstack1l_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫ⇙"))
    @classmethod
    @error_handler(class_method=True)
    def bstack11111l1l1l_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1lll11ll_opy_({
            bstack1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ⇚"): bstack1l_opy_ (u"ࠨࡅࡅࡘࡘ࡫ࡳࡴ࡫ࡲࡲࡈࡸࡥࡢࡶࡨࡨࠬ⇛"),
            bstack1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ⇜"): {
                bstack1l_opy_ (u"ࠥࡹࡺ࡯ࡤࠣ⇝"): cls.current_test_uuid(),
                bstack1l_opy_ (u"ࠦ࡮ࡴࡴࡦࡩࡵࡥࡹ࡯࡯࡯ࡵࠥ⇞"): cls.bstack1l1llll1_opy_(driver)
            }
        })
    @classmethod
    def bstack1lll11l1_opy_(cls, event: str, bstack1l111lll_opy_: bstack1l1111l1_opy_):
        bstack1l11l1ll_opy_ = {
            bstack1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ⇟"): event,
            bstack1l111lll_opy_.event_key(): bstack1l111lll_opy_.bstack1l111l11_opy_(event)
        }
        cls.bstack1lll11ll_opy_(bstack1l11l1ll_opy_)
        result = getattr(bstack1l111lll_opy_, bstack1l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⇠"), None)
        if event == bstack1l_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨ⇡"):
            threading.current_thread().bstackTestMeta = {bstack1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ⇢"): bstack1l_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪ⇣")}
        elif event == bstack1l_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ⇤"):
            threading.current_thread().bstackTestMeta = {bstack1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ⇥"): getattr(result, bstack1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⇦"), bstack1l_opy_ (u"࠭ࠧ⇧"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ⇨"), None) is None or os.environ[bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ⇩")] == bstack1l_opy_ (u"ࠤࡱࡹࡱࡲࠢ⇪")) and (os.environ.get(bstack1l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ⇫"), None) is None or os.environ[bstack1l_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ⇬")] == bstack1l_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ⇭")):
            return False
        return True
    @staticmethod
    def bstack1llll1l11l11_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1ll1lll1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack1l_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬ⇮"): bstack1l_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪ⇯"),
            bstack1l_opy_ (u"ࠨ࡚࠰ࡆࡘ࡚ࡁࡄࡍ࠰ࡘࡊ࡙ࡔࡐࡒࡖࠫ⇰"): bstack1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ⇱")
        }
        if os.environ.get(bstack1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ⇲"), None):
            headers[bstack1l_opy_ (u"ࠫࡆࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫ⇳")] = bstack1l_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥࢁࡽࠨ⇴").format(os.environ[bstack1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠥ⇵")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack1l_opy_ (u"ࠧࡼࡿ࠲ࡿࢂ࠭⇶").format(bstack1llll1l11ll1_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack1l_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ⇷"), None)
    @staticmethod
    def bstack1l1llll1_opy_(driver):
        return {
            bstack111l1ll1l11_opy_(): bstack1111lll11ll_opy_(driver)
        }
    @staticmethod
    def bstack1llll11lllll_opy_(exception_info, report):
        return [{bstack1l_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬ⇸"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack11111l11ll_opy_(typename):
        if bstack1l_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨ⇹") in typename:
            return bstack1l_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧ⇺")
        return bstack1l_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨ⇻")