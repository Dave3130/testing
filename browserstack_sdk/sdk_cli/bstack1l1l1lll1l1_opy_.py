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
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1l11l1_opy_ import bstack1lllll1111l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import (
    bstack1lllllll1l1_opy_,
    bstack1llllll1l11_opy_,
    bstack1lllll111l1_opy_,
)
from bstack_utils.helper import  bstack1l11l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll11l1ll_opy_ import bstack1llll1lllll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll111l1l_opy_, bstack1lll1l1llll_opy_, bstack1lll1lll111_opy_, bstack1ll1l1l1ll1_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack1111l1111l_opy_ import bstack1111ll1lll_opy_
from browserstack_sdk.sdk_cli.bstack1lll111ll1l_opy_ import bstack1lll11l11l1_opy_
from bstack_utils.percy import bstack11111lll1l_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l11ll11lll_opy_(bstack1lllll1111l_opy_):
    def __init__(self, bstack11lllll11l1_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11lllll11l1_opy_ = bstack11lllll11l1_opy_
        self.percy = bstack11111lll1l_opy_()
        self.bstack1l11lll1ll_opy_ = bstack1111ll1lll_opy_()
        self.bstack11lllll111l_opy_()
        bstack1llll1lllll_opy_.bstack1llll1l1l11_opy_((bstack1lllllll1l1_opy_.bstack1lllll11l1l_opy_, bstack1llllll1l11_opy_.PRE), self.bstack11lllll11ll_opy_)
        TestFramework.bstack1llll1l1l11_opy_((bstack1llll111l1l_opy_.TEST, bstack1lll1lll111_opy_.POST), self.bstack1lll1l11l11_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l11l111_opy_(self, instance: bstack1lllll111l1_opy_, driver: object):
        bstack1l11ll1111l_opy_ = TestFramework.bstack1l11l111lll_opy_(instance.context)
        for t in bstack1l11ll1111l_opy_:
            bstack1lll1111l11_opy_ = TestFramework.get_state(t, bstack1lll11l11l1_opy_.bstack1lll1ll1ll1_opy_, [])
            if any(instance is d[1] for d in bstack1lll1111l11_opy_) or instance == driver:
                return t
    def bstack11lllll11ll_opy_(
        self,
        f: bstack1llll1lllll_opy_,
        driver: object,
        exec: Tuple[bstack1lllll111l1_opy_, str],
        bstack1llll1l1lll_opy_: Tuple[bstack1lllllll1l1_opy_, bstack1llllll1l11_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1llll1lllll_opy_.bstack1l1lll11l11_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1llll1lllll_opy_.bstack1llllllllll_opy_, 0)
            bstack1ll11ll11ll_opy_ = self.bstack1l11l11l111_opy_(instance, driver)
            bstack11llll1llll_opy_ = TestFramework.get_state(bstack1ll11ll11ll_opy_, TestFramework.bstack1ll11l1l1l1_opy_, None)
            if not bstack11llll1llll_opy_:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡲࡲࡤࡶࡲࡦࡡࡨࡼࡪࡩࡵࡵࡧ࠽ࠤࡷ࡫ࡴࡶࡴࡱ࡭ࡳ࡭ࠠࡢࡵࠣࡷࡪࡹࡳࡪࡱࡱࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡾ࡫ࡴࠡࡵࡷࡥࡷࡺࡥࡥࠤᔺ"))
                return
            driver_command = f.bstack1l1ll1ll1l1_opy_(*args)
            for command in bstack1l1llll111_opy_:
                if command == driver_command:
                    self.bstack11lllll111_opy_(driver, platform_index)
            bstack1l111l1l1l_opy_ = self.percy.bstack1ll11l111_opy_()
            if driver_command in bstack1ll1llll1l_opy_[bstack1l111l1l1l_opy_]:
                self.bstack1l11lll1ll_opy_.bstack1ll11l1l1_opy_(bstack11llll1llll_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠥࡳࡳࡥࡰࡳࡧࡢࡩࡽ࡫ࡣࡶࡶࡨ࠾ࠥ࡫ࡲࡳࡱࡵࠦᔻ"), e)
    def bstack1lll1l11l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack111l1111l_opy_ import bstack1llllllll1l_opy_
        bstack1lll1111l11_opy_ = f.get_state(instance, bstack1lll11l11l1_opy_.bstack1lll1ll1ll1_opy_, [])
        if not bstack1lll1111l11_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᔼ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠧࠨᔽ"))
            return
        if len(bstack1lll1111l11_opy_) > 1:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠࡼ࡮ࡨࡲ࠭ࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᔾ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠢࠣᔿ"))
        bstack1lll111ll11_opy_, bstack1lll1l1l11l_opy_ = bstack1lll1111l11_opy_[0]
        driver = bstack1lll111ll11_opy_()
        if not driver:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᕀ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠤࠥᕁ"))
            return
        bstack11lllll1l11_opy_ = {
            TestFramework.bstack1ll111l111l_opy_: bstack1lllll1l_opy_ (u"ࠥࡸࡪࡹࡴࠡࡰࡤࡱࡪࠨᕂ"),
            TestFramework.bstack1lll1lll1ll_opy_: bstack1lllll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࠢࡸࡹ࡮ࡪࠢᕃ"),
            TestFramework.bstack1ll11l1l1l1_opy_: bstack1lllll1l_opy_ (u"ࠧࡺࡥࡴࡶࠣࡶࡪࡸࡵ࡯ࠢࡱࡥࡲ࡫ࠢᕄ")
        }
        bstack11lllll1ll1_opy_ = { key: f.get_state(instance, key) for key in bstack11lllll1l11_opy_ }
        bstack11lllll1lll_opy_ = [key for key, value in bstack11lllll1ll1_opy_.items() if not value]
        if bstack11lllll1lll_opy_:
            for key in bstack11lllll1lll_opy_:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠤᕅ") + str(key) + bstack1lllll1l_opy_ (u"ࠢࠣᕆ"))
            return
        platform_index = f.get_state(instance, bstack1llll1lllll_opy_.bstack1llllllllll_opy_, 0)
        if self.bstack11lllll11l1_opy_.percy_capture_mode == bstack1lllll1l_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥᕇ"):
            bstack1l1ll1ll1_opy_ = bstack11lllll1ll1_opy_.get(TestFramework.bstack1ll11l1l1l1_opy_) + bstack1lllll1l_opy_ (u"ࠤ࠰ࡸࡪࡹࡴࡤࡣࡶࡩࠧᕈ")
            bstack1ll111ll1l1_opy_ = bstack1llllllll1l_opy_.bstack1ll11l111l1_opy_(EVENTS.bstack11llll1lll1_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack1l1ll1ll1_opy_,
                bstack1l1l1l1l1_opy_=bstack11lllll1ll1_opy_[TestFramework.bstack1ll111l111l_opy_],
                bstack11l1llllll_opy_=bstack11lllll1ll1_opy_[TestFramework.bstack1lll1lll1ll_opy_],
                bstack1l11111111_opy_=platform_index
            )
            bstack1llllllll1l_opy_.end(EVENTS.bstack11llll1lll1_opy_.value, bstack1ll111ll1l1_opy_+bstack1lllll1l_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᕉ"), bstack1ll111ll1l1_opy_+bstack1lllll1l_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᕊ"), True, None, None, None, None, test_name=bstack1l1ll1ll1_opy_)
    def bstack11lllll111_opy_(self, driver, platform_index):
        if self.bstack1l11lll1ll_opy_.bstack111l111ll1_opy_() is True or self.bstack1l11lll1ll_opy_.capturing() is True:
            return
        self.bstack1l11lll1ll_opy_.bstack1l1l1ll111_opy_()
        while not self.bstack1l11lll1ll_opy_.bstack111l111ll1_opy_():
            bstack11llll1llll_opy_ = self.bstack1l11lll1ll_opy_.bstack111ll111l1_opy_()
            self.bstack1ll11l1l11_opy_(driver, bstack11llll1llll_opy_, platform_index)
        self.bstack1l11lll1ll_opy_.bstack1ll1l1l111_opy_()
    def bstack1ll11l1l11_opy_(self, driver, bstack1l1ll11ll_opy_, platform_index, test=None):
        from bstack_utils.bstack111l1111l_opy_ import bstack1llllllll1l_opy_
        bstack1ll111ll1l1_opy_ = bstack1llllllll1l_opy_.bstack1ll11l111l1_opy_(EVENTS.bstack11l1l1lll1_opy_.value)
        if test != None:
            bstack1l1l1l1l1_opy_ = getattr(test, bstack1lllll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᕋ"), None)
            bstack11l1llllll_opy_ = getattr(test, bstack1lllll1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᕌ"), None)
            PercySDK.screenshot(driver, bstack1l1ll11ll_opy_, bstack1l1l1l1l1_opy_=bstack1l1l1l1l1_opy_, bstack11l1llllll_opy_=bstack11l1llllll_opy_, bstack1l11111111_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack1l1ll11ll_opy_)
        bstack1llllllll1l_opy_.end(EVENTS.bstack11l1l1lll1_opy_.value, bstack1ll111ll1l1_opy_+bstack1lllll1l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᕍ"), bstack1ll111ll1l1_opy_+bstack1lllll1l_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᕎ"), True, None, None, None, None, test_name=bstack1l1ll11ll_opy_)
    def bstack11lllll111l_opy_(self):
        os.environ[bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟ࠧᕏ")] = str(self.bstack11lllll11l1_opy_.success)
        os.environ[bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࡠࡅࡄࡔ࡙࡛ࡒࡆࡡࡐࡓࡉࡋࠧᕐ")] = str(self.bstack11lllll11l1_opy_.percy_capture_mode)
        self.percy.bstack11lllll1111_opy_(self.bstack11lllll11l1_opy_.is_percy_auto_enabled)
        self.percy.bstack11lllll1l1l_opy_(self.bstack11lllll11l1_opy_.percy_build_id)