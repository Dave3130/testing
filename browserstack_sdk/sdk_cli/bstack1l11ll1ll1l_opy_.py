# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllll1l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1111111lll_opy_ import (
    bstack1llllll1111_opy_,
    bstack1llll1l11ll_opy_,
    bstack1llll1l1l11_opy_,
)
from bstack_utils.helper import  bstack1l1lllll_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1l11_opy_ import bstack1llll1l11l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll111l_opy_, bstack1lll1l11l11_opy_, bstack1lll1l1ll11_opy_, bstack1ll1l11ll1l_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack1llll11l1l_opy_ import bstack1ll1lll11l_opy_
from browserstack_sdk.sdk_cli.bstack1lll111ll1l_opy_ import bstack1lll111llll_opy_
from bstack_utils.percy import bstack111l111ll_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l1l1l11l11_opy_(bstack1lllll1l1l1_opy_):
    def __init__(self, bstack11lllllll11_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11lllllll11_opy_ = bstack11lllllll11_opy_
        self.percy = bstack111l111ll_opy_()
        self.bstack1l1l1111l1_opy_ = bstack1ll1lll11l_opy_()
        self.bstack11lllllllll_opy_()
        bstack1llll1l11l1_opy_.bstack1lllll11111_opy_((bstack1llllll1111_opy_.bstack1llllll1lll_opy_, bstack1llll1l11ll_opy_.PRE), self.bstack11llllllll1_opy_)
        TestFramework.bstack1lllll11111_opy_((bstack1lll1ll111l_opy_.TEST, bstack1lll1l1ll11_opy_.POST), self.bstack1lll1l1l1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l1lll1l_opy_(self, instance: bstack1llll1l1l11_opy_, driver: object):
        bstack1l11l111lll_opy_ = TestFramework.bstack1l11l1ll1l1_opy_(instance.context)
        for t in bstack1l11l111lll_opy_:
            bstack1lll11ll1ll_opy_ = TestFramework.get_state(t, bstack1lll111llll_opy_.bstack1llll111ll1_opy_, [])
            if any(instance is d[1] for d in bstack1lll11ll1ll_opy_) or instance == driver:
                return t
    def bstack11llllllll1_opy_(
        self,
        f: bstack1llll1l11l1_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        bstack1lllllll1ll_opy_: Tuple[bstack1llllll1111_opy_, bstack1llll1l11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1llll1l11l1_opy_.bstack1l1lll11lll_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1llll1l11l1_opy_.bstack1lllll1111l_opy_, 0)
            bstack1ll111lll11_opy_ = self.bstack1l11l1lll1l_opy_(instance, driver)
            bstack11lllll1ll1_opy_ = TestFramework.get_state(bstack1ll111lll11_opy_, TestFramework.bstack1ll1l1llll1_opy_, None)
            if not bstack11lllll1ll1_opy_:
                self.logger.debug(bstack11111_opy_ (u"ࠤࡲࡲࡤࡶࡲࡦࡡࡨࡼࡪࡩࡵࡵࡧ࠽ࠤࡷ࡫ࡴࡶࡴࡱ࡭ࡳ࡭ࠠࡢࡵࠣࡷࡪࡹࡳࡪࡱࡱࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡾ࡫ࡴࠡࡵࡷࡥࡷࡺࡥࡥࠤᔉ"))
                return
            driver_command = f.bstack1l1lll11l11_opy_(*args)
            for command in bstack1l111llll_opy_:
                if command == driver_command:
                    self.bstack111llll1l1_opy_(driver, platform_index)
            bstack11lll1ll1_opy_ = self.percy.bstack1l11l11ll1_opy_()
            if driver_command in bstack1l11lll1l_opy_[bstack11lll1ll1_opy_]:
                self.bstack1l1l1111l1_opy_.bstack1ll1111lll_opy_(bstack11lllll1ll1_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack11111_opy_ (u"ࠥࡳࡳࡥࡰࡳࡧࡢࡩࡽ࡫ࡣࡶࡶࡨ࠾ࠥ࡫ࡲࡳࡱࡵࠦᔊ"), e)
    def bstack1lll1l1l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack11l1ll11l_opy_ import bstack111111l11l_opy_
        bstack1lll11ll1ll_opy_ = f.get_state(instance, bstack1lll111llll_opy_.bstack1llll111ll1_opy_, [])
        if not bstack1lll11ll1ll_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᔋ") + str(kwargs) + bstack11111_opy_ (u"ࠧࠨᔌ"))
            return
        if len(bstack1lll11ll1ll_opy_) > 1:
            self.logger.debug(bstack11111_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠࡼ࡮ࡨࡲ࠭ࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᔍ") + str(kwargs) + bstack11111_opy_ (u"ࠢࠣᔎ"))
        bstack1lll11ll111_opy_, bstack1lll1ll1111_opy_ = bstack1lll11ll1ll_opy_[0]
        driver = bstack1lll11ll111_opy_()
        if not driver:
            self.logger.debug(bstack11111_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᔏ") + str(kwargs) + bstack11111_opy_ (u"ࠤࠥᔐ"))
            return
        bstack11llllll1l1_opy_ = {
            TestFramework.bstack1ll111ll1l1_opy_: bstack11111_opy_ (u"ࠥࡸࡪࡹࡴࠡࡰࡤࡱࡪࠨᔑ"),
            TestFramework.bstack1lll11lllll_opy_: bstack11111_opy_ (u"ࠦࡹ࡫ࡳࡵࠢࡸࡹ࡮ࡪࠢᔒ"),
            TestFramework.bstack1ll1l1llll1_opy_: bstack11111_opy_ (u"ࠧࡺࡥࡴࡶࠣࡶࡪࡸࡵ࡯ࠢࡱࡥࡲ࡫ࠢᔓ")
        }
        bstack11lllllll1l_opy_ = { key: f.get_state(instance, key) for key in bstack11llllll1l1_opy_ }
        bstack11lllll1lll_opy_ = [key for key, value in bstack11lllllll1l_opy_.items() if not value]
        if bstack11lllll1lll_opy_:
            for key in bstack11lllll1lll_opy_:
                self.logger.debug(bstack11111_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠤᔔ") + str(key) + bstack11111_opy_ (u"ࠢࠣᔕ"))
            return
        platform_index = f.get_state(instance, bstack1llll1l11l1_opy_.bstack1lllll1111l_opy_, 0)
        if self.bstack11lllllll11_opy_.percy_capture_mode == bstack11111_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥᔖ"):
            bstack1l111lll1_opy_ = bstack11lllllll1l_opy_.get(TestFramework.bstack1ll1l1llll1_opy_) + bstack11111_opy_ (u"ࠤ࠰ࡸࡪࡹࡴࡤࡣࡶࡩࠧᔗ")
            bstack1l1lllll1ll_opy_ = bstack111111l11l_opy_.bstack1ll1l11l1l1_opy_(EVENTS.bstack11llllll111_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack1l111lll1_opy_,
                bstack11llll1l1l_opy_=bstack11lllllll1l_opy_[TestFramework.bstack1ll111ll1l1_opy_],
                bstack11111l11ll_opy_=bstack11lllllll1l_opy_[TestFramework.bstack1lll11lllll_opy_],
                bstack1l1l11l111_opy_=platform_index
            )
            bstack111111l11l_opy_.end(EVENTS.bstack11llllll111_opy_.value, bstack1l1lllll1ll_opy_+bstack11111_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᔘ"), bstack1l1lllll1ll_opy_+bstack11111_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᔙ"), True, None, None, None, None, test_name=bstack1l111lll1_opy_)
    def bstack111llll1l1_opy_(self, driver, platform_index):
        if self.bstack1l1l1111l1_opy_.bstack1l1l11lll_opy_() is True or self.bstack1l1l1111l1_opy_.capturing() is True:
            return
        self.bstack1l1l1111l1_opy_.bstack1ll11l11l1_opy_()
        while not self.bstack1l1l1111l1_opy_.bstack1l1l11lll_opy_():
            bstack11lllll1ll1_opy_ = self.bstack1l1l1111l1_opy_.bstack11lll1lll1_opy_()
            self.bstack1lll11l1l_opy_(driver, bstack11lllll1ll1_opy_, platform_index)
        self.bstack1l1l1111l1_opy_.bstack1l1l1111ll_opy_()
    def bstack1lll11l1l_opy_(self, driver, bstack11l11ll11_opy_, platform_index, test=None):
        from bstack_utils.bstack11l1ll11l_opy_ import bstack111111l11l_opy_
        bstack1l1lllll1ll_opy_ = bstack111111l11l_opy_.bstack1ll1l11l1l1_opy_(EVENTS.bstack1l1l1lllll_opy_.value)
        if test != None:
            bstack11llll1l1l_opy_ = getattr(test, bstack11111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᔚ"), None)
            bstack11111l11ll_opy_ = getattr(test, bstack11111_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᔛ"), None)
            PercySDK.screenshot(driver, bstack11l11ll11_opy_, bstack11llll1l1l_opy_=bstack11llll1l1l_opy_, bstack11111l11ll_opy_=bstack11111l11ll_opy_, bstack1l1l11l111_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack11l11ll11_opy_)
        bstack111111l11l_opy_.end(EVENTS.bstack1l1l1lllll_opy_.value, bstack1l1lllll1ll_opy_+bstack11111_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᔜ"), bstack1l1lllll1ll_opy_+bstack11111_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᔝ"), True, None, None, None, None, test_name=bstack11l11ll11_opy_)
    def bstack11lllllllll_opy_(self):
        os.environ[bstack11111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟ࠧᔞ")] = str(self.bstack11lllllll11_opy_.success)
        os.environ[bstack11111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࡠࡅࡄࡔ࡙࡛ࡒࡆࡡࡐࡓࡉࡋࠧᔟ")] = str(self.bstack11lllllll11_opy_.percy_capture_mode)
        self.percy.bstack11llllll1ll_opy_(self.bstack11lllllll11_opy_.is_percy_auto_enabled)
        self.percy.bstack11llllll11l_opy_(self.bstack11lllllll11_opy_.percy_build_id)