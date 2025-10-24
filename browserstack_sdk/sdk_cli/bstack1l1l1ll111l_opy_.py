# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1111111l1l_opy_ import bstack1llllll1111_opy_
from browserstack_sdk.sdk_cli.bstack11111111ll_opy_ import (
    bstack1lllllll11l_opy_,
    bstack1llll1l11l1_opy_,
    bstack1lllll111ll_opy_,
)
from bstack_utils.helper import  bstack1ll11l1l_opy_
from browserstack_sdk.sdk_cli.bstack1111111111_opy_ import bstack1llll1lll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1lll1_opy_, bstack1lll1l11111_opy_, bstack1lll1ll1111_opy_, bstack1ll1111111l_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack11l1l11l1l_opy_ import bstack1ll1l1111_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l111l_opy_ import bstack1lll111lll1_opy_
from bstack_utils.percy import bstack1ll1l11l1_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1l1l1lll11l_opy_(bstack1llllll1111_opy_):
    def __init__(self, bstack11lllll1lll_opy_: Dict[str, str]):
        super().__init__()
        self.bstack11lllll1lll_opy_ = bstack11lllll1lll_opy_
        self.percy = bstack1ll1l11l1_opy_()
        self.bstack1ll111111l_opy_ = bstack1ll1l1111_opy_()
        self.bstack11lllll11ll_opy_()
        bstack1llll1lll1l_opy_.bstack1llll1l1l11_opy_((bstack1lllllll11l_opy_.bstack1111111l11_opy_, bstack1llll1l11l1_opy_.PRE), self.bstack11lllll1l11_opy_)
        TestFramework.bstack1llll1l1l11_opy_((bstack1lll1l1lll1_opy_.TEST, bstack1lll1ll1111_opy_.POST), self.bstack1lll1ll1lll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l111l11_opy_(self, instance: bstack1lllll111ll_opy_, driver: object):
        bstack1l11l1l1ll1_opy_ = TestFramework.bstack1l11l11111l_opy_(instance.context)
        for t in bstack1l11l1l1ll1_opy_:
            bstack1lll11111ll_opy_ = TestFramework.get_state(t, bstack1lll111lll1_opy_.bstack1llll11l1l1_opy_, [])
            if any(instance is d[1] for d in bstack1lll11111ll_opy_) or instance == driver:
                return t
    def bstack11lllll1l11_opy_(
        self,
        f: bstack1llll1lll1l_opy_,
        driver: object,
        exec: Tuple[bstack1lllll111ll_opy_, str],
        bstack1lllllll1l1_opy_: Tuple[bstack1lllllll11l_opy_, bstack1llll1l11l1_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1llll1lll1l_opy_.bstack1l1ll1ll11l_opy_(method_name):
                return
            platform_index = f.get_state(instance, bstack1llll1lll1l_opy_.bstack1lllll11111_opy_, 0)
            bstack1ll11l1lll1_opy_ = self.bstack1l11l111l11_opy_(instance, driver)
            bstack11lllll1111_opy_ = TestFramework.get_state(bstack1ll11l1lll1_opy_, TestFramework.bstack1ll11l11111_opy_, None)
            if not bstack11lllll1111_opy_:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠧࡵ࡮ࡠࡲࡵࡩࡤ࡫ࡸࡦࡥࡸࡸࡪࡀࠠࡳࡧࡷࡹࡷࡴࡩ࡯ࡩࠣࡥࡸࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡪࡵࠣࡲࡴࡺࠠࡺࡧࡷࠤࡸࡺࡡࡳࡶࡨࡨࠧᔯ"))
                return
            driver_command = f.bstack1l1lll111ll_opy_(*args)
            for command in bstack1l11ll1lll_opy_:
                if command == driver_command:
                    self.bstack1l111ll1ll_opy_(driver, platform_index)
            bstack1l1llll1l1_opy_ = self.percy.bstack1l1ll11111_opy_()
            if driver_command in bstack111lll1ll1_opy_[bstack1l1llll1l1_opy_]:
                self.bstack1ll111111l_opy_.bstack1lll111l11_opy_(bstack11lllll1111_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack11l11l1_opy_ (u"ࠨ࡯࡯ࡡࡳࡶࡪࡥࡥࡹࡧࡦࡹࡹ࡫࠺ࠡࡧࡵࡶࡴࡸࠢᔰ"), e)
    def bstack1lll1ll1lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11111_opy_,
        bstack1lllllll1l1_opy_: Tuple[bstack1lll1l1lll1_opy_, bstack1lll1ll1111_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack11ll111ll1_opy_ import bstack1lllll1l111_opy_
        bstack1lll11111ll_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll11l1l1_opy_, [])
        if not bstack1lll11111ll_opy_:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᔱ") + str(kwargs) + bstack11l11l1_opy_ (u"ࠣࠤᔲ"))
            return
        if len(bstack1lll11111ll_opy_) > 1:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᔳ") + str(kwargs) + bstack11l11l1_opy_ (u"ࠥࠦᔴ"))
        bstack1lll11l11l1_opy_, bstack1lll11ll1ll_opy_ = bstack1lll11111ll_opy_[0]
        driver = bstack1lll11l11l1_opy_()
        if not driver:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᔵ") + str(kwargs) + bstack11l11l1_opy_ (u"ࠧࠨᔶ"))
            return
        bstack11llllll111_opy_ = {
            TestFramework.bstack1ll1l1ll1ll_opy_: bstack11l11l1_opy_ (u"ࠨࡴࡦࡵࡷࠤࡳࡧ࡭ࡦࠤᔷ"),
            TestFramework.bstack1lll1l11l11_opy_: bstack11l11l1_opy_ (u"ࠢࡵࡧࡶࡸࠥࡻࡵࡪࡦࠥᔸ"),
            TestFramework.bstack1ll11l11111_opy_: bstack11l11l1_opy_ (u"ࠣࡶࡨࡷࡹࠦࡲࡦࡴࡸࡲࠥࡴࡡ࡮ࡧࠥᔹ")
        }
        bstack11lllll111l_opy_ = { key: f.get_state(instance, key) for key in bstack11llllll111_opy_ }
        bstack11lllll1ll1_opy_ = [key for key, value in bstack11lllll111l_opy_.items() if not value]
        if bstack11lllll1ll1_opy_:
            for key in bstack11lllll1ll1_opy_:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࠧᔺ") + str(key) + bstack11l11l1_opy_ (u"ࠥࠦᔻ"))
            return
        platform_index = f.get_state(instance, bstack1llll1lll1l_opy_.bstack1lllll11111_opy_, 0)
        if self.bstack11lllll1lll_opy_.percy_capture_mode == bstack11l11l1_opy_ (u"ࠦࡹ࡫ࡳࡵࡥࡤࡷࡪࠨᔼ"):
            bstack1l1ll1l111_opy_ = bstack11lllll111l_opy_.get(TestFramework.bstack1ll11l11111_opy_) + bstack11l11l1_opy_ (u"ࠧ࠳ࡴࡦࡵࡷࡧࡦࡹࡥࠣᔽ")
            bstack1ll11llllll_opy_ = bstack1lllll1l111_opy_.bstack1ll11111ll1_opy_(EVENTS.bstack11llllll11l_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack1l1ll1l111_opy_,
                bstack1l1111l111_opy_=bstack11lllll111l_opy_[TestFramework.bstack1ll1l1ll1ll_opy_],
                bstack111lll111l_opy_=bstack11lllll111l_opy_[TestFramework.bstack1lll1l11l11_opy_],
                bstack11ll111l11_opy_=platform_index
            )
            bstack1lllll1l111_opy_.end(EVENTS.bstack11llllll11l_opy_.value, bstack1ll11llllll_opy_+bstack11l11l1_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᔾ"), bstack1ll11llllll_opy_+bstack11l11l1_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᔿ"), True, None, None, None, None, test_name=bstack1l1ll1l111_opy_)
    def bstack1l111ll1ll_opy_(self, driver, platform_index):
        if self.bstack1ll111111l_opy_.bstack111ll1lll1_opy_() is True or self.bstack1ll111111l_opy_.capturing() is True:
            return
        self.bstack1ll111111l_opy_.bstack1ll1111l1l_opy_()
        while not self.bstack1ll111111l_opy_.bstack111ll1lll1_opy_():
            bstack11lllll1111_opy_ = self.bstack1ll111111l_opy_.bstack11l1ll1111_opy_()
            self.bstack11ll1lll1_opy_(driver, bstack11lllll1111_opy_, platform_index)
        self.bstack1ll111111l_opy_.bstack11l1ll11l1_opy_()
    def bstack11ll1lll1_opy_(self, driver, bstack1ll111l11l_opy_, platform_index, test=None):
        from bstack_utils.bstack11ll111ll1_opy_ import bstack1lllll1l111_opy_
        bstack1ll11llllll_opy_ = bstack1lllll1l111_opy_.bstack1ll11111ll1_opy_(EVENTS.bstack1l1l1111l_opy_.value)
        if test != None:
            bstack1l1111l111_opy_ = getattr(test, bstack11l11l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᕀ"), None)
            bstack111lll111l_opy_ = getattr(test, bstack11l11l1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᕁ"), None)
            PercySDK.screenshot(driver, bstack1ll111l11l_opy_, bstack1l1111l111_opy_=bstack1l1111l111_opy_, bstack111lll111l_opy_=bstack111lll111l_opy_, bstack11ll111l11_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack1ll111l11l_opy_)
        bstack1lllll1l111_opy_.end(EVENTS.bstack1l1l1111l_opy_.value, bstack1ll11llllll_opy_+bstack11l11l1_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᕂ"), bstack1ll11llllll_opy_+bstack11l11l1_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᕃ"), True, None, None, None, None, test_name=bstack1ll111l11l_opy_)
    def bstack11lllll11ll_opy_(self):
        os.environ[bstack11l11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࠪᕄ")] = str(self.bstack11lllll1lll_opy_.success)
        os.environ[bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࡣࡈࡇࡐࡕࡗࡕࡉࡤࡓࡏࡅࡇࠪᕅ")] = str(self.bstack11lllll1lll_opy_.percy_capture_mode)
        self.percy.bstack11lllll1l1l_opy_(self.bstack11lllll1lll_opy_.is_percy_auto_enabled)
        self.percy.bstack11lllll11l1_opy_(self.bstack11lllll1lll_opy_.percy_build_id)