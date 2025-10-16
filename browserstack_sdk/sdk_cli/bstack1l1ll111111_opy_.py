# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1111111111_opy_ import bstack1llll1ll11l_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1lll_opy_ import (
    bstack1llll1ll1ll_opy_,
    bstack1lllll1lll1_opy_,
    bstack1111111l11_opy_,
)
from bstack_utils.helper import  bstack1lll1l11_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1ll1_opy_ import bstack1lllll1ll11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11l1ll_opy_, bstack1lll1l11l11_opy_, bstack1llll1l11l1_opy_, bstack1ll1l1l1ll1_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack11l1111lll_opy_ import bstack111lll11l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll11l111l_opy_
from bstack_utils.percy import bstack1ll1l1ll1l_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l11lll1111_opy_(bstack1llll1ll11l_opy_):
    def __init__(self, bstack1l11111111l_opy_: Dict[str, str]):
        super().__init__()
        self.bstack1l11111111l_opy_ = bstack1l11111111l_opy_
        self.percy = bstack1ll1l1ll1l_opy_()
        self.bstack11l1l11ll_opy_ = bstack111lll11l1_opy_()
        self.bstack11lllllll1l_opy_()
        bstack1lllll1ll11_opy_.bstack11111111ll_opy_((bstack1llll1ll1ll_opy_.bstack1lllll1l1l1_opy_, bstack1lllll1lll1_opy_.PRE), self.bstack11llllll1l1_opy_)
        TestFramework.bstack11111111ll_opy_((bstack1llll11l1ll_opy_.TEST, bstack1llll1l11l1_opy_.POST), self.bstack1llll111l1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l1ll11l_opy_(self, instance: bstack1111111l11_opy_, driver: object):
        bstack1l11ll1l1l1_opy_ = TestFramework.bstack1l11l11ll1l_opy_(instance.context)
        for t in bstack1l11ll1l1l1_opy_:
            bstack1lll11ll111_opy_ = TestFramework.get_state(t, bstack1lll11l111l_opy_.bstack1llll1111ll_opy_, [])
            if any(instance is d[1] for d in bstack1lll11ll111_opy_) or instance == driver:
                return t
    def bstack11llllll1l1_opy_(
        self,
        f: bstack1lllll1ll11_opy_,
        driver: object,
        exec: Tuple[bstack1111111l11_opy_, str],
        bstack1lllll111ll_opy_: Tuple[bstack1llll1ll1ll_opy_, bstack1lllll1lll1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1lllll1ll11_opy_.bstack1l1ll1lllll_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1lllll1ll11_opy_.bstack1111111ll1_opy_, 0)
            bstack1l1lllll1ll_opy_ = self.bstack1l11l1ll11l_opy_(instance, driver)
            bstack1l111111111_opy_ = TestFramework.get_state(bstack1l1lllll1ll_opy_, TestFramework.bstack1ll11ll1lll_opy_, None)
            if not bstack1l111111111_opy_:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡵ࡮ࡠࡲࡵࡩࡤ࡫ࡸࡦࡥࡸࡸࡪࡀࠠࡳࡧࡷࡹࡷࡴࡩ࡯ࡩࠣࡥࡸࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡪࡵࠣࡲࡴࡺࠠࡺࡧࡷࠤࡸࡺࡡࡳࡶࡨࡨࠧᔚ"))
                return
            driver_command = f.bstack1l1lll111l1_opy_(*args)
            for command in bstack11ll11lll1_opy_:
                if command == driver_command:
                    self.bstack11l11ll1l_opy_(driver, platform_index)
            bstack1ll11111ll_opy_ = self.percy.bstack1l1l1l1l1_opy_()
            if driver_command in bstack111ll1l1ll_opy_[bstack1ll11111ll_opy_]:
                self.bstack11l1l11ll_opy_.bstack1ll1l1l11l_opy_(bstack1l111111111_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠨ࡯࡯ࡡࡳࡶࡪࡥࡥࡹࡧࡦࡹࡹ࡫࠺ࠡࡧࡵࡶࡴࡸࠢᔛ"), e)
    def bstack1llll111l1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllll111ll_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1llll1l11l1_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack11l11l1111_opy_ import bstack1lllllllll1_opy_
        bstack1lll11ll111_opy_ = f.get_state(instance, bstack1lll11l111l_opy_.bstack1llll1111ll_opy_, [])
        if not bstack1lll11ll111_opy_:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᔜ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠣࠤᔝ"))
            return
        if len(bstack1lll11ll111_opy_) > 1:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᔞ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠥࠦᔟ"))
        bstack1lll11l11ll_opy_, bstack1lll1ll11l1_opy_ = bstack1lll11ll111_opy_[0]
        driver = bstack1lll11l11ll_opy_()
        if not driver:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᔠ") + str(kwargs) + bstack1lllll1_opy_ (u"ࠧࠨᔡ"))
            return
        bstack1l1111111l1_opy_ = {
            TestFramework.bstack1ll11l111ll_opy_: bstack1lllll1_opy_ (u"ࠨࡴࡦࡵࡷࠤࡳࡧ࡭ࡦࠤᔢ"),
            TestFramework.bstack1lll1lllll1_opy_: bstack1lllll1_opy_ (u"ࠢࡵࡧࡶࡸࠥࡻࡵࡪࡦࠥᔣ"),
            TestFramework.bstack1ll11ll1lll_opy_: bstack1lllll1_opy_ (u"ࠣࡶࡨࡷࡹࠦࡲࡦࡴࡸࡲࠥࡴࡡ࡮ࡧࠥᔤ")
        }
        bstack11llllll11l_opy_ = { key: f.get_state(instance, key) for key in bstack1l1111111l1_opy_ }
        bstack11llllll1ll_opy_ = [key for key, value in bstack11llllll11l_opy_.items() if not value]
        if bstack11llllll1ll_opy_:
            for key in bstack11llllll1ll_opy_:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࠧᔥ") + str(key) + bstack1lllll1_opy_ (u"ࠥࠦᔦ"))
            return
        platform_index = f.get_state(instance, bstack1lllll1ll11_opy_.bstack1111111ll1_opy_, 0)
        if self.bstack1l11111111l_opy_.percy_capture_mode == bstack1lllll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡥࡤࡷࡪࠨᔧ"):
            bstack11l1ll11l_opy_ = bstack11llllll11l_opy_.get(TestFramework.bstack1ll11ll1lll_opy_) + bstack1lllll1_opy_ (u"ࠧ࠳ࡴࡦࡵࡷࡧࡦࡹࡥࠣᔨ")
            bstack1ll1l1l1111_opy_ = bstack1lllllllll1_opy_.bstack1ll11111ll1_opy_(EVENTS.bstack11llllllll1_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack11l1ll11l_opy_,
                bstack1ll1ll1111_opy_=bstack11llllll11l_opy_[TestFramework.bstack1ll11l111ll_opy_],
                bstack11l1lll1l_opy_=bstack11llllll11l_opy_[TestFramework.bstack1lll1lllll1_opy_],
                bstack1l1l1l1lll_opy_=platform_index
            )
            bstack1lllllllll1_opy_.end(EVENTS.bstack11llllllll1_opy_.value, bstack1ll1l1l1111_opy_+bstack1lllll1_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᔩ"), bstack1ll1l1l1111_opy_+bstack1lllll1_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᔪ"), True, None, None, None, None, test_name=bstack11l1ll11l_opy_)
    def bstack11l11ll1l_opy_(self, driver, platform_index):
        if self.bstack11l1l11ll_opy_.bstack111l11111_opy_() is True or self.bstack11l1l11ll_opy_.capturing() is True:
            return
        self.bstack11l1l11ll_opy_.bstack1lll11l1ll_opy_()
        while not self.bstack11l1l11ll_opy_.bstack111l11111_opy_():
            bstack1l111111111_opy_ = self.bstack11l1l11ll_opy_.bstack1111l1111l_opy_()
            self.bstack1l111l1ll_opy_(driver, bstack1l111111111_opy_, platform_index)
        self.bstack11l1l11ll_opy_.bstack1ll11ll11_opy_()
    def bstack1l111l1ll_opy_(self, driver, bstack1111lll11l_opy_, platform_index, test=None):
        from bstack_utils.bstack11l11l1111_opy_ import bstack1lllllllll1_opy_
        bstack1ll1l1l1111_opy_ = bstack1lllllllll1_opy_.bstack1ll11111ll1_opy_(EVENTS.bstack1ll1llll11_opy_.value)
        if test != None:
            bstack1ll1ll1111_opy_ = getattr(test, bstack1lllll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᔫ"), None)
            bstack11l1lll1l_opy_ = getattr(test, bstack1lllll1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᔬ"), None)
            PercySDK.screenshot(driver, bstack1111lll11l_opy_, bstack1ll1ll1111_opy_=bstack1ll1ll1111_opy_, bstack11l1lll1l_opy_=bstack11l1lll1l_opy_, bstack1l1l1l1lll_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack1111lll11l_opy_)
        bstack1lllllllll1_opy_.end(EVENTS.bstack1ll1llll11_opy_.value, bstack1ll1l1l1111_opy_+bstack1lllll1_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᔭ"), bstack1ll1l1l1111_opy_+bstack1lllll1_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᔮ"), True, None, None, None, None, test_name=bstack1111lll11l_opy_)
    def bstack11lllllll1l_opy_(self):
        os.environ[bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࠪᔯ")] = str(self.bstack1l11111111l_opy_.success)
        os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࡣࡈࡇࡐࡕࡗࡕࡉࡤࡓࡏࡅࡇࠪᔰ")] = str(self.bstack1l11111111l_opy_.percy_capture_mode)
        self.percy.bstack11lllllll11_opy_(self.bstack1l11111111l_opy_.is_percy_auto_enabled)
        self.percy.bstack11lllllllll_opy_(self.bstack1l11111111l_opy_.percy_build_id)