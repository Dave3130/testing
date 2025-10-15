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
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1lll1l_opy_
from browserstack_sdk.sdk_cli.bstack1lllll11ll1_opy_ import (
    bstack1lllll11l1l_opy_,
    bstack1111111lll_opy_,
    bstack1llllllll1l_opy_,
)
from bstack_utils.helper import  bstack1l1l1l1l_opy_
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import bstack1lllll11l11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11l1ll_opy_, bstack1lll1l1l1ll_opy_, bstack1lll1llll11_opy_, bstack1ll11lll111_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack11llll11ll_opy_ import bstack1111l1llll_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l1ll_opy_ import bstack1lll11l1ll1_opy_
from bstack_utils.percy import bstack1ll1llll1_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l11lll1ll1_opy_(bstack1llll1lll1l_opy_):
    def __init__(self, bstack11llllll111_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11llllll111_opy_ = bstack11llllll111_opy_
        self.percy = bstack1ll1llll1_opy_()
        self.bstack11111l1l1_opy_ = bstack1111l1llll_opy_()
        self.bstack1l111111111_opy_()
        bstack1lllll11l11_opy_.bstack1lllll1l11l_opy_((bstack1lllll11l1l_opy_.bstack1111111111_opy_, bstack1111111lll_opy_.PRE), self.bstack11llllll11l_opy_)
        TestFramework.bstack1lllll1l11l_opy_((bstack1llll11l1ll_opy_.TEST, bstack1lll1llll11_opy_.POST), self.bstack1llll11l111_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l1ll1l1_opy_(self, instance: bstack1llllllll1l_opy_, driver: object):
        bstack1l11l1l11ll_opy_ = TestFramework.bstack1l11l11l11l_opy_(instance.context)
        for t in bstack1l11l1l11ll_opy_:
            bstack1lll11l11l1_opy_ = TestFramework.get_state(t, bstack1lll11l1ll1_opy_.bstack1llll1l11l1_opy_, [])
            if any(instance is d[1] for d in bstack1lll11l11l1_opy_) or instance == driver:
                return t
    def bstack11llllll11l_opy_(
        self,
        f: bstack1lllll11l11_opy_,
        driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        bstack1llllll111l_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1lllll11l11_opy_.bstack1l1lll1l1ll_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1lllll11l11_opy_.bstack1lllllllll1_opy_, 0)
            bstack1ll1111111l_opy_ = self.bstack1l11l1ll1l1_opy_(instance, driver)
            bstack11llllll1ll_opy_ = TestFramework.get_state(bstack1ll1111111l_opy_, TestFramework.bstack1ll111l11ll_opy_, None)
            if not bstack11llllll1ll_opy_:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠨ࡯࡯ࡡࡳࡶࡪࡥࡥࡹࡧࡦࡹࡹ࡫࠺ࠡࡴࡨࡸࡺࡸ࡮ࡪࡰࡪࠤࡦࡹࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡ࡫ࡶࠤࡳࡵࡴࠡࡻࡨࡸࠥࡹࡴࡢࡴࡷࡩࡩࠨᔔ"))
                return
            driver_command = f.bstack1l1lll1l11l_opy_(*args)
            for command in bstack1ll11ll1l1_opy_:
                if command == driver_command:
                    self.bstack1llll1l111_opy_(driver, platform_index)
            bstack11l11l1ll1_opy_ = self.percy.bstack11lllll1ll_opy_()
            if driver_command in bstack1l11lll1l_opy_[bstack11l11l1ll1_opy_]:
                self.bstack11111l1l1_opy_.bstack11l1l111ll_opy_(bstack11llllll1ll_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack1ll1l_opy_ (u"ࠢࡰࡰࡢࡴࡷ࡫࡟ࡦࡺࡨࡧࡺࡺࡥ࠻ࠢࡨࡶࡷࡵࡲࠣᔕ"), e)
    def bstack1llll11l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack111l11llll_opy_ import bstack1llll1l1l11_opy_
        bstack1lll11l11l1_opy_ = f.get_state(instance, bstack1lll11l1ll1_opy_.bstack1llll1l11l1_opy_, [])
        if not bstack1lll11l11l1_opy_:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᔖ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠤࠥᔗ"))
            return
        if len(bstack1lll11l11l1_opy_) > 1:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᔘ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠦࠧᔙ"))
        bstack1lll11ll111_opy_, bstack1lll1ll1l1l_opy_ = bstack1lll11l11l1_opy_[0]
        driver = bstack1lll11ll111_opy_()
        if not driver:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᔚ") + str(kwargs) + bstack1ll1l_opy_ (u"ࠨࠢᔛ"))
            return
        bstack11llllll1l1_opy_ = {
            TestFramework.bstack1ll1l11l11l_opy_: bstack1ll1l_opy_ (u"ࠢࡵࡧࡶࡸࠥࡴࡡ࡮ࡧࠥᔜ"),
            TestFramework.bstack1llll11ll1l_opy_: bstack1ll1l_opy_ (u"ࠣࡶࡨࡷࡹࠦࡵࡶ࡫ࡧࠦᔝ"),
            TestFramework.bstack1ll111l11ll_opy_: bstack1ll1l_opy_ (u"ࠤࡷࡩࡸࡺࠠࡳࡧࡵࡹࡳࠦ࡮ࡢ࡯ࡨࠦᔞ")
        }
        bstack11lllllll11_opy_ = { key: f.get_state(instance, key) for key in bstack11llllll1l1_opy_ }
        bstack11lllll1lll_opy_ = [key for key, value in bstack11lllllll11_opy_.items() if not value]
        if bstack11lllll1lll_opy_:
            for key in bstack11lllll1lll_opy_:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࠨᔟ") + str(key) + bstack1ll1l_opy_ (u"ࠦࠧᔠ"))
            return
        platform_index = f.get_state(instance, bstack1lllll11l11_opy_.bstack1lllllllll1_opy_, 0)
        if self.bstack11llllll111_opy_.percy_capture_mode == bstack1ll1l_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢᔡ"):
            bstack1l11111l11_opy_ = bstack11lllllll11_opy_.get(TestFramework.bstack1ll111l11ll_opy_) + bstack1ll1l_opy_ (u"ࠨ࠭ࡵࡧࡶࡸࡨࡧࡳࡦࠤᔢ")
            bstack1l1lllll111_opy_ = bstack1llll1l1l11_opy_.bstack1ll1ll1111l_opy_(EVENTS.bstack11lllllll1l_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack1l11111l11_opy_,
                bstack11ll11lll1_opy_=bstack11lllllll11_opy_[TestFramework.bstack1ll1l11l11l_opy_],
                bstack11111lll1_opy_=bstack11lllllll11_opy_[TestFramework.bstack1llll11ll1l_opy_],
                bstack1111l1111l_opy_=platform_index
            )
            bstack1llll1l1l11_opy_.end(EVENTS.bstack11lllllll1l_opy_.value, bstack1l1lllll111_opy_+bstack1ll1l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᔣ"), bstack1l1lllll111_opy_+bstack1ll1l_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᔤ"), True, None, None, None, None, test_name=bstack1l11111l11_opy_)
    def bstack1llll1l111_opy_(self, driver, platform_index):
        if self.bstack11111l1l1_opy_.bstack11ll1111l_opy_() is True or self.bstack11111l1l1_opy_.capturing() is True:
            return
        self.bstack11111l1l1_opy_.bstack111lll1ll_opy_()
        while not self.bstack11111l1l1_opy_.bstack11ll1111l_opy_():
            bstack11llllll1ll_opy_ = self.bstack11111l1l1_opy_.bstack1lllllll1l_opy_()
            self.bstack11ll111ll1_opy_(driver, bstack11llllll1ll_opy_, platform_index)
        self.bstack11111l1l1_opy_.bstack11l1lllll_opy_()
    def bstack11ll111ll1_opy_(self, driver, bstack1ll11l111_opy_, platform_index, test=None):
        from bstack_utils.bstack111l11llll_opy_ import bstack1llll1l1l11_opy_
        bstack1l1lllll111_opy_ = bstack1llll1l1l11_opy_.bstack1ll1ll1111l_opy_(EVENTS.bstack1111l11ll_opy_.value)
        if test != None:
            bstack11ll11lll1_opy_ = getattr(test, bstack1ll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᔥ"), None)
            bstack11111lll1_opy_ = getattr(test, bstack1ll1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨᔦ"), None)
            PercySDK.screenshot(driver, bstack1ll11l111_opy_, bstack11ll11lll1_opy_=bstack11ll11lll1_opy_, bstack11111lll1_opy_=bstack11111lll1_opy_, bstack1111l1111l_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack1ll11l111_opy_)
        bstack1llll1l1l11_opy_.end(EVENTS.bstack1111l11ll_opy_.value, bstack1l1lllll111_opy_+bstack1ll1l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᔧ"), bstack1l1lllll111_opy_+bstack1ll1l_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᔨ"), True, None, None, None, None, test_name=bstack1ll11l111_opy_)
    def bstack1l111111111_opy_(self):
        os.environ[bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࠫᔩ")] = str(self.bstack11llllll111_opy_.success)
        os.environ[bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࡤࡉࡁࡑࡖࡘࡖࡊࡥࡍࡐࡆࡈࠫᔪ")] = str(self.bstack11llllll111_opy_.percy_capture_mode)
        self.percy.bstack11llllllll1_opy_(self.bstack11llllll111_opy_.is_percy_auto_enabled)
        self.percy.bstack11lllllllll_opy_(self.bstack11llllll111_opy_.percy_build_id)