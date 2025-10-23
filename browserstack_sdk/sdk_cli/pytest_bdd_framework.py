# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1lll1111111_opy_ import bstack1ll1lll1111_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll1lll1ll_opy_ import bstack1ll1111l1l1_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1llll111lll_opy_,
    bstack1lll1lll1l1_opy_,
    bstack1lll1lll11l_opy_,
    bstack1l1llllllll_opy_,
    bstack1ll111lll11_opy_,
)
import traceback
from bstack_utils.helper import bstack1ll11llllll_opy_
from bstack_utils.bstack1l11ll11l1_opy_ import bstack1llllll1lll_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1ll11l1ll1l_opy_ import bstack1ll1l1ll111_opy_
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll11llll1_opy_
bstack1ll111l1l1l_opy_ = bstack1ll11llllll_opy_()
bstack1ll1l1l1lll_opy_ = bstack111111l_opy_ (u"࡛ࠧࡰ࡭ࡱࡤࡨࡪࡪࡁࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶ࠱ࠧᇮ")
bstack1ll11l11111_opy_ = bstack111111l_opy_ (u"ࠨࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠤᇯ")
bstack1ll11l1l11l_opy_ = bstack111111l_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠨᇰ")
bstack1ll111111l1_opy_ = 1.0
_1ll111l1ll1_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1ll1l1lll1l_opy_ = bstack111111l_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠣᇱ")
    bstack1ll1l11ll11_opy_ = bstack111111l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡸࡥࡳࡵࡣࡵࡸࡪࡪࠢᇲ")
    bstack1ll111l11l1_opy_ = bstack111111l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡪࡲࡳࡰࡹ࡟ࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࠤᇳ")
    bstack1ll11l1111l_opy_ = bstack111111l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟࡭ࡣࡶࡸࡤࡹࡴࡢࡴࡷࡩࡩࠨᇴ")
    bstack1ll1l111lll_opy_ = bstack111111l_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠ࡮ࡤࡷࡹࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤࠣᇵ")
    bstack1ll1111lll1_opy_: bool
    bstack1lll11lllll_opy_: bstack1lll11llll1_opy_  = None
    bstack1ll1111ll1l_opy_ = [
        bstack1llll111lll_opy_.BEFORE_ALL,
        bstack1llll111lll_opy_.AFTER_ALL,
        bstack1llll111lll_opy_.BEFORE_EACH,
        bstack1llll111lll_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll11lll11l_opy_: Dict[str, str],
        bstack1ll11l11ll1_opy_: List[str]=[bstack111111l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥᇶ")],
        bstack1lll11lllll_opy_: bstack1lll11llll1_opy_ = None,
        bstack111111111l_opy_=None
    ):
        super().__init__(bstack1ll11l11ll1_opy_, bstack1ll11lll11l_opy_, bstack1lll11lllll_opy_)
        self.bstack1ll1111lll1_opy_ = any(bstack111111l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠦᇷ") in item.lower() for item in bstack1ll11l11ll1_opy_)
        self.bstack111111111l_opy_ = bstack111111111l_opy_
    def track_event(
        self,
        context: bstack1l1llllllll_opy_,
        test_framework_state: bstack1llll111lll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1llll111lll_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1ll1111ll1l_opy_:
            bstack1ll1111l1l1_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1llll111lll_opy_.NONE:
            self.logger.warning(bstack111111l_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡥࡥࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࠤࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂࠦࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥ࠾ࠤᇸ") + str(test_hook_state) + bstack111111l_opy_ (u"ࠤࠥᇹ"))
            return
        if not self.bstack1ll1111lll1_opy_:
            self.logger.warning(bstack111111l_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲࡸࡻࡰࡱࡱࡵࡸࡪࡪࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡀࠦᇺ") + str(str(self.bstack1ll11l11ll1_opy_)) + bstack111111l_opy_ (u"ࠦࠧᇻ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack111111l_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᇼ") + str(kwargs) + bstack111111l_opy_ (u"ࠨࠢᇽ"))
            return
        instance = self.__1ll1l1l1l1l_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack111111l_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡢࡴࡪࡷࡂࠨᇾ") + str(args) + bstack111111l_opy_ (u"ࠣࠤᇿ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll1111ll1l_opy_ and test_hook_state == bstack1lll1lll11l_opy_.PRE:
                bstack1ll1l1ll1ll_opy_ = bstack1llllll1lll_opy_.bstack1ll1l1l11ll_opy_(EVENTS.bstack1ll1111ll_opy_.value)
                name = str(EVENTS.bstack1ll1111ll_opy_.name)+bstack111111l_opy_ (u"ࠤ࠽ࠦሀ")+str(test_framework_state.name)
                TestFramework.bstack1ll111l1111_opy_(instance, name, bstack1ll1l1ll1ll_opy_)
        except Exception as e:
            self.logger.debug(bstack111111l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡳࡴࡱࠠࡦࡴࡵࡳࡷࠦࡰࡳࡧ࠽ࠤࢀࢃࠢሁ").format(e))
        try:
            if test_framework_state == bstack1llll111lll_opy_.TEST:
                if not TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll1l11l11l_opy_) and test_hook_state == bstack1lll1lll11l_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1ll1l11llll_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack111111l_opy_ (u"ࠦࡱࡵࡡࡥࡧࡧࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦሂ") + str(test_hook_state) + bstack111111l_opy_ (u"ࠧࠨሃ"))
                if test_hook_state == bstack1lll1lll11l_opy_.PRE and not TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll111l1l11_opy_):
                    TestFramework.bstack1llll1lll1l_opy_(instance, TestFramework.bstack1ll111l1l11_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1ll1l1llll1_opy_(instance, args)
                    self.logger.debug(bstack111111l_opy_ (u"ࠨࡳࡦࡶࠣࡸࡪࡹࡴ࠮ࡵࡷࡥࡷࡺࠠࡧࡱࡵࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦሄ") + str(test_hook_state) + bstack111111l_opy_ (u"ࠢࠣህ"))
                elif test_hook_state == bstack1lll1lll11l_opy_.POST and not TestFramework.bstack1lllllll11l_opy_(instance, TestFramework.bstack1ll11l1l1ll_opy_):
                    TestFramework.bstack1llll1lll1l_opy_(instance, TestFramework.bstack1ll11l1l1ll_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack111111l_opy_ (u"ࠣࡵࡨࡸࠥࡺࡥࡴࡶ࠰ࡩࡳࡪࠠࡧࡱࡵࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡵࡩ࡫࠮ࠩࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦሆ") + str(test_hook_state) + bstack111111l_opy_ (u"ࠤࠥሇ"))
            elif test_framework_state == bstack1llll111lll_opy_.STEP:
                if test_hook_state == bstack1lll1lll11l_opy_.PRE:
                    PytestBDDFramework.__1ll111lllll_opy_(instance, args)
                elif test_hook_state == bstack1lll1lll11l_opy_.POST:
                    PytestBDDFramework.__1ll11111ll1_opy_(instance, args)
            elif test_framework_state == bstack1llll111lll_opy_.LOG and test_hook_state == bstack1lll1lll11l_opy_.POST:
                PytestBDDFramework.__1ll1l111l1l_opy_(instance, *args)
            elif test_framework_state == bstack1llll111lll_opy_.LOG_REPORT and test_hook_state == bstack1lll1lll11l_opy_.POST:
                self.__1l1lllll1l1_opy_(instance, *args)
                self.__1ll111ll1l1_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1ll1111ll1l_opy_:
                self.__1ll11llll11_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack111111l_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࠦለ") + str(instance.ref()) + bstack111111l_opy_ (u"ࠦࠧሉ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1ll1l11l1l1_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1ll1111ll1l_opy_ and test_hook_state == bstack1lll1lll11l_opy_.POST:
                name = str(EVENTS.bstack1ll1111ll_opy_.name)+bstack111111l_opy_ (u"ࠧࡀࠢሊ")+str(test_framework_state.name)
                bstack1ll1l1ll1ll_opy_ = TestFramework.bstack1ll111lll1l_opy_(instance, name)
                bstack1llllll1lll_opy_.end(EVENTS.bstack1ll1111ll_opy_.value, bstack1ll1l1ll1ll_opy_+bstack111111l_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨላ"), bstack1ll1l1ll1ll_opy_+bstack111111l_opy_ (u"ࠢ࠻ࡧࡱࡨࠧሌ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack111111l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡩࡱࡲ࡯ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣል").format(e))
    def bstack1ll1l1lll11_opy_(self):
        return self.bstack1ll1111lll1_opy_
    def __1ll11ll1l1l_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack111111l_opy_ (u"ࠤࡪࡩࡹࡥࡲࡦࡵࡸࡰࡹࠨሎ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll11111l11_opy_(rep, [bstack111111l_opy_ (u"ࠥࡻ࡭࡫࡮ࠣሏ"), bstack111111l_opy_ (u"ࠦࡴࡻࡴࡤࡱࡰࡩࠧሐ"), bstack111111l_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧሑ"), bstack111111l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨሒ"), bstack111111l_opy_ (u"ࠢࡴ࡭࡬ࡴࡵ࡫ࡤࠣሓ"), bstack111111l_opy_ (u"ࠣ࡮ࡲࡲ࡬ࡸࡥࡱࡴࡷࡩࡽࡺࠢሔ")])
        return None
    def __1l1lllll1l1_opy_(self, instance: bstack1lll1lll1l1_opy_, *args):
        result = self.__1ll11ll1l1l_opy_(*args)
        if not result:
            return
        failure = None
        bstack11111l111l_opy_ = None
        if result.get(bstack111111l_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥሕ"), None) == bstack111111l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥሖ") and len(args) > 1 and getattr(args[1], bstack111111l_opy_ (u"ࠦࡪࡾࡣࡪࡰࡩࡳࠧሗ"), None) is not None:
            failure = [{bstack111111l_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨመ"): [args[1].excinfo.exconly(), result.get(bstack111111l_opy_ (u"ࠨ࡬ࡰࡰࡪࡶࡪࡶࡲࡵࡧࡻࡸࠧሙ"), None)]}]
            bstack11111l111l_opy_ = bstack111111l_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣሚ") if bstack111111l_opy_ (u"ࠣࡃࡶࡷࡪࡸࡴࡪࡱࡱࠦማ") in getattr(args[1].excinfo, bstack111111l_opy_ (u"ࠤࡷࡽࡵ࡫࡮ࡢ࡯ࡨࠦሜ"), bstack111111l_opy_ (u"ࠥࠦም")) else bstack111111l_opy_ (u"࡚ࠦࡴࡨࡢࡰࡧࡰࡪࡪࡅࡳࡴࡲࡶࠧሞ")
        bstack1ll111l111l_opy_ = result.get(bstack111111l_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨሟ"), TestFramework.bstack1ll11llll1l_opy_)
        if bstack1ll111l111l_opy_ != TestFramework.bstack1ll11llll1l_opy_:
            TestFramework.bstack1llll1lll1l_opy_(instance, TestFramework.bstack1ll1l1111ll_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll1l11l111_opy_(instance, {
            TestFramework.bstack1lll1ll11ll_opy_: failure,
            TestFramework.bstack1ll111ll111_opy_: bstack11111l111l_opy_,
            TestFramework.bstack1lll1ll1ll1_opy_: bstack1ll111l111l_opy_,
        })
    def __1ll1l1l1l1l_opy_(
        self,
        context: bstack1l1llllllll_opy_,
        test_framework_state: bstack1llll111lll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1llll111lll_opy_.SETUP_FIXTURE:
            instance = self.__1ll111llll1_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll11ll1111_opy_ bstack1ll1ll1111l_opy_ this to be bstack111111l_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨሠ")
            if test_framework_state == bstack1llll111lll_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll1l11111l_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1llll111lll_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack111111l_opy_ (u"ࠢ࡯ࡱࡧࡩࠧሡ"), None), bstack111111l_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣሢ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack111111l_opy_ (u"ࠤࡱࡳࡩ࡫ࠢሣ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack111111l_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥሤ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1ll11ll1lll_opy_(target) if target else None
        return instance
    def __1ll11llll11_opy_(
        self,
        instance: bstack1lll1lll1l1_opy_,
        test_framework_state: bstack1llll111lll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1ll1l11lll1_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll1l11ll11_opy_, {})
        if not key in bstack1ll1l11lll1_opy_:
            bstack1ll1l11lll1_opy_[key] = []
        bstack1l1llllll11_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll111l11l1_opy_, {})
        if not key in bstack1l1llllll11_opy_:
            bstack1l1llllll11_opy_[key] = []
        bstack1ll1111ll11_opy_ = {
            PytestBDDFramework.bstack1ll1l11ll11_opy_: bstack1ll1l11lll1_opy_,
            PytestBDDFramework.bstack1ll111l11l1_opy_: bstack1l1llllll11_opy_,
        }
        if test_hook_state == bstack1lll1lll11l_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack111111l_opy_ (u"ࠦࡰ࡫ࡹࠣሥ"): key,
                TestFramework.bstack1ll1l1111l1_opy_: uuid4().__str__(),
                TestFramework.bstack1ll11l111ll_opy_: TestFramework.bstack1ll11ll1l11_opy_,
                TestFramework.bstack1ll11lllll1_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll11l1l1l1_opy_: [],
                TestFramework.bstack1ll11l1l111_opy_: hook_name,
                TestFramework.bstack1ll1l1ll1l1_opy_: bstack1ll1l1ll111_opy_.bstack1ll11l1lll1_opy_()
            }
            bstack1ll1l11lll1_opy_[key].append(hook)
            bstack1ll1111ll11_opy_[PytestBDDFramework.bstack1ll11l1111l_opy_] = key
        elif test_hook_state == bstack1lll1lll11l_opy_.POST:
            bstack1ll1ll11111_opy_ = bstack1ll1l11lll1_opy_.get(key, [])
            hook = bstack1ll1ll11111_opy_.pop() if bstack1ll1ll11111_opy_ else None
            if hook:
                result = self.__1ll11ll1l1l_opy_(*args)
                if result:
                    bstack1l1lllllll1_opy_ = result.get(bstack111111l_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨሦ"), TestFramework.bstack1ll11ll1l11_opy_)
                    if bstack1l1lllllll1_opy_ != TestFramework.bstack1ll11ll1l11_opy_:
                        hook[TestFramework.bstack1ll11l111ll_opy_] = bstack1l1lllllll1_opy_
                hook[TestFramework.bstack1ll111ll1ll_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll1l1ll1l1_opy_] = bstack1ll1l1ll111_opy_.bstack1ll11l1lll1_opy_()
                self.bstack1ll1l11ll1l_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll11l11l1l_opy_, [])
                self.bstack1ll11111111_opy_(instance, logs)
                bstack1l1llllll11_opy_[key].append(hook)
                bstack1ll1111ll11_opy_[PytestBDDFramework.bstack1ll1l111lll_opy_] = key
        TestFramework.bstack1ll1l11l111_opy_(instance, bstack1ll1111ll11_opy_)
        self.logger.debug(bstack111111l_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡮࡯ࡰ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࡂࢁ࡫ࡦࡻࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡪࡲࡳࡰࡹ࡟ࡴࡶࡤࡶࡹ࡫ࡤ࠾ࡽ࡫ࡳࡴࡱࡳࡠࡵࡷࡥࡷࡺࡥࡥࡿࠣ࡬ࡴࡵ࡫ࡴࡡࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡁࠧሧ") + str(bstack1l1llllll11_opy_) + bstack111111l_opy_ (u"ࠢࠣረ"))
    def __1ll111llll1_opy_(
        self,
        context: bstack1l1llllllll_opy_,
        test_framework_state: bstack1llll111lll_opy_,
        test_hook_state: bstack1lll1lll11l_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll11111l11_opy_(args[0], [bstack111111l_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢሩ"), bstack111111l_opy_ (u"ࠤࡤࡶ࡬ࡴࡡ࡮ࡧࠥሪ"), bstack111111l_opy_ (u"ࠥࡴࡦࡸࡡ࡮ࡵࠥራ"), bstack111111l_opy_ (u"ࠦ࡮ࡪࡳࠣሬ"), bstack111111l_opy_ (u"ࠧࡻ࡮ࡪࡶࡷࡩࡸࡺࠢር"), bstack111111l_opy_ (u"ࠨࡢࡢࡵࡨ࡭ࡩࠨሮ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack111111l_opy_ (u"ࠢࡴࡥࡲࡴࡪࠨሯ")) else fixturedef.get(bstack111111l_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢሰ"), None)
        fixturename = request.fixturename if hasattr(request, bstack111111l_opy_ (u"ࠤࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࠢሱ")) else None
        node = request.node if hasattr(request, bstack111111l_opy_ (u"ࠥࡲࡴࡪࡥࠣሲ")) else None
        target = request.node.nodeid if hasattr(node, bstack111111l_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦሳ")) else None
        baseid = fixturedef.get(bstack111111l_opy_ (u"ࠧࡨࡡࡴࡧ࡬ࡨࠧሴ"), None) or bstack111111l_opy_ (u"ࠨࠢስ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack111111l_opy_ (u"ࠢࡠࡲࡼࡪࡺࡴࡣࡪࡶࡨࡱࠧሶ")):
            target = PytestBDDFramework.__1ll1l111111_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack111111l_opy_ (u"ࠣ࡮ࡲࡧࡦࡺࡩࡰࡰࠥሷ")) else None
            if target and not TestFramework.bstack1ll11ll1lll_opy_(target):
                self.__1ll1l11111l_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack111111l_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡨࡺࡪࡴࡴ࠻ࠢࡩࡥࡱࡲࡢࡢࡥ࡮ࠤࡹࡧࡲࡨࡧࡷࡁࢀࡺࡡࡳࡩࡨࡸࢂࠦࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࡁࢀ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࢀࠤࡳࡵࡤࡦ࠿ࡾࡲࡴࡪࡥࡾࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࠦሸ") + str(test_hook_state) + bstack111111l_opy_ (u"ࠥࠦሹ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack111111l_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡪ࡮ࡾࡴࡶࡴࡨࡣࡪࡼࡥ࡯ࡶ࠽ࠤࡺࡴࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡪࡥࡧ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡨࡪ࡬ࡽࠡࡵࡦࡳࡵ࡫࠽ࡼࡵࡦࡳࡵ࡫ࡽࠡࡶࡤࡶ࡬࡫ࡴ࠾ࠤሺ") + str(target) + bstack111111l_opy_ (u"ࠧࠨሻ"))
            return None
        instance = TestFramework.bstack1ll11ll1lll_opy_(target)
        if not instance:
            self.logger.warning(bstack111111l_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡪࡤࡲࡩࡲࡥࡥࠢࡨࡺࡪࡴࡴ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿ࠱ࡿࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࢃࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥࡨࡡࡴࡧ࡬ࡨࡂࢁࡢࡢࡵࡨ࡭ࡩࢃࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣሼ") + str(target) + bstack111111l_opy_ (u"ࠢࠣሽ"))
            return None
        bstack1ll11l1llll_opy_ = TestFramework.get_state(instance, PytestBDDFramework.bstack1ll1l1lll1l_opy_, {})
        if os.getenv(bstack111111l_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡇࡋ࡛ࡘ࡚ࡘࡅࡔࠤሾ"), bstack111111l_opy_ (u"ࠤ࠴ࠦሿ")) == bstack111111l_opy_ (u"ࠥ࠵ࠧቀ"):
            bstack1ll11l11l11_opy_ = bstack111111l_opy_ (u"ࠦ࠿ࠨቁ").join((scope, fixturename))
            bstack1ll1l1l1111_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll1111111l_opy_ = {
                bstack111111l_opy_ (u"ࠧࡱࡥࡺࠤቂ"): bstack1ll11l11l11_opy_,
                bstack111111l_opy_ (u"ࠨࡴࡢࡩࡶࠦቃ"): PytestBDDFramework.__1ll11l111l1_opy_(request.node, scenario),
                bstack111111l_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥࠣቄ"): fixturedef,
                bstack111111l_opy_ (u"ࠣࡵࡦࡳࡵ࡫ࠢቅ"): scope,
                bstack111111l_opy_ (u"ࠤࡷࡽࡵ࡫ࠢቆ"): None,
            }
            try:
                if test_hook_state == bstack1lll1lll11l_opy_.POST and callable(getattr(args[-1], bstack111111l_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡳࡧࡶࡹࡱࡺࠢቇ"), None)):
                    bstack1ll1111111l_opy_[bstack111111l_opy_ (u"ࠦࡹࡿࡰࡦࠤቈ")] = TestFramework.bstack1ll1l1ll11l_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1lll11l_opy_.PRE:
                bstack1ll1111111l_opy_[bstack111111l_opy_ (u"ࠧࡻࡵࡪࡦࠥ቉")] = uuid4().__str__()
                bstack1ll1111111l_opy_[PytestBDDFramework.bstack1ll11lllll1_opy_] = bstack1ll1l1l1111_opy_
            elif test_hook_state == bstack1lll1lll11l_opy_.POST:
                bstack1ll1111111l_opy_[PytestBDDFramework.bstack1ll111ll1ll_opy_] = bstack1ll1l1l1111_opy_
            if bstack1ll11l11l11_opy_ in bstack1ll11l1llll_opy_:
                bstack1ll11l1llll_opy_[bstack1ll11l11l11_opy_].update(bstack1ll1111111l_opy_)
                self.logger.debug(bstack111111l_opy_ (u"ࠨࡵࡱࡦࡤࡸࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡃࠢቊ") + str(bstack1ll11l1llll_opy_[bstack1ll11l11l11_opy_]) + bstack111111l_opy_ (u"ࠢࠣቋ"))
            else:
                bstack1ll11l1llll_opy_[bstack1ll11l11l11_opy_] = bstack1ll1111111l_opy_
                self.logger.debug(bstack111111l_opy_ (u"ࠣࡵࡤࡺࡪࡪࠠࡧ࡫ࡻࡸࡺࡸࡥ࡯ࡣࡰࡩࡂࢁࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥ࡬ࡩࡹࡶࡸࡶࡪࡃࡻࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࢃࠠࡵࡴࡤࡧࡰ࡫ࡤࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࡀࠦቌ") + str(len(bstack1ll11l1llll_opy_)) + bstack111111l_opy_ (u"ࠤࠥቍ"))
        TestFramework.bstack1llll1lll1l_opy_(instance, PytestBDDFramework.bstack1ll1l1lll1l_opy_, bstack1ll11l1llll_opy_)
        self.logger.debug(bstack111111l_opy_ (u"ࠥࡷࡦࡼࡥࡥࠢࡩ࡭ࡽࡺࡵࡳࡧࡶࡁࢀࡲࡥ࡯ࠪࡷࡶࡦࡩ࡫ࡦࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࡷ࠮ࢃࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࠥ቎") + str(instance.ref()) + bstack111111l_opy_ (u"ࠦࠧ቏"))
        return instance
    def __1ll1l11111l_opy_(
        self,
        context: bstack1l1llllllll_opy_,
        test_framework_state: bstack1llll111lll_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1lll1111_opy_.create_context(target)
        ob = bstack1lll1lll1l1_opy_(ctx, self.bstack1ll11l11ll1_opy_, self.bstack1ll11lll11l_opy_, test_framework_state)
        TestFramework.bstack1ll1l11l111_opy_(ob, {
            TestFramework.bstack1llll1111l1_opy_: context.test_framework_name,
            TestFramework.bstack1llll1l11l1_opy_: context.test_framework_version,
            TestFramework.bstack1ll1ll11l11_opy_: [],
            PytestBDDFramework.bstack1ll1l1lll1l_opy_: {},
            PytestBDDFramework.bstack1ll111l11l1_opy_: {},
            PytestBDDFramework.bstack1ll1l11ll11_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llll1lll1l_opy_(ob, TestFramework.bstack1ll111l1lll_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llll1lll1l_opy_(ob, TestFramework.bstack1llllllll1l_opy_, context.platform_index)
        TestFramework.bstack1llll111l1l_opy_[ctx.id] = ob
        self.logger.debug(bstack111111l_opy_ (u"ࠧࡹࡡࡷࡧࡧࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࠦࡣࡵࡺ࠱࡭ࡩࡃࡻࡤࡶࡻ࠲࡮ࡪࡽࠡࡶࡤࡶ࡬࡫ࡴ࠾ࡽࡷࡥࡷ࡭ࡥࡵࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶࡁࠧቐ") + str(TestFramework.bstack1llll111l1l_opy_.keys()) + bstack111111l_opy_ (u"ࠨࠢቑ"))
        return ob
    @staticmethod
    def __1ll1l1llll1_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack111111l_opy_ (u"ࠧࡪࡦࠪቒ"): id(step),
                bstack111111l_opy_ (u"ࠨࡶࡨࡼࡹ࠭ቓ"): step.name,
                bstack111111l_opy_ (u"ࠩ࡮ࡩࡾࡽ࡯ࡳࡦࠪቔ"): step.keyword,
            })
        meta = {
            bstack111111l_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࠫቕ"): {
                bstack111111l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩቖ"): feature.name,
                bstack111111l_opy_ (u"ࠬࡶࡡࡵࡪࠪ቗"): feature.filename,
                bstack111111l_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫቘ"): feature.description
            },
            bstack111111l_opy_ (u"ࠧࡴࡥࡨࡲࡦࡸࡩࡰࠩ቙"): {
                bstack111111l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ቚ"): scenario.name
            },
            bstack111111l_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨቛ"): steps,
            bstack111111l_opy_ (u"ࠪࡩࡽࡧ࡭ࡱ࡮ࡨࡷࠬቜ"): PytestBDDFramework.__1l1llll1ll1_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1ll1l1lllll_opy_: meta
            }
        )
    def bstack1ll1l11ll1l_opy_(self, hook: Dict[str, Any]) -> None:
        bstack111111l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡒࡵࡳࡨ࡫ࡳࡴࡧࡶࠤࡹ࡮ࡥࠡࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡶ࡭ࡲ࡯࡬ࡢࡴࠣࡸࡴࠦࡴࡩࡧࠣࡎࡦࡼࡡࠡ࡫ࡰࡴࡱ࡫࡭ࡦࡰࡷࡥࡹ࡯࡯࡯࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡙࡮ࡩࡴࠢࡰࡩࡹ࡮࡯ࡥ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡅ࡫ࡩࡨࡱࡳࠡࡶ࡫ࡩࠥࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬ࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࡮ࡴࡳࡪࡦࡨࠤࢃ࠵࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠵ࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡋࡵࡲࠡࡧࡤࡧ࡭ࠦࡦࡪ࡮ࡨࠤ࡮ࡴࠠࡩࡱࡲ࡯ࡤࡲࡥࡷࡧ࡯ࡣ࡫࡯࡬ࡦࡵ࠯ࠤࡷ࡫ࡰ࡭ࡣࡦࡩࡸࠦࠢࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠥࠤࡼ࡯ࡴࡩࠢࠥࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠨࠠࡪࡰࠣ࡭ࡹࡹࠠࡱࡣࡷ࡬࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡎ࡬ࠠࡢࠢࡩ࡭ࡱ࡫ࠠࡪࡰࠣࡸ࡭࡫ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡱࡦࡺࡣࡩࡧࡶࠤࡦࠦ࡭ࡰࡦ࡬ࡪ࡮࡫ࡤࠡࡪࡲࡳࡰ࠳࡬ࡦࡸࡨࡰࠥ࡬ࡩ࡭ࡧ࠯ࠤ࡮ࡺࠠࡤࡴࡨࡥࡹ࡫ࡳࠡࡣࠣࡐࡴ࡭ࡅ࡯ࡶࡵࡽࠥࡵࡢ࡫ࡧࡦࡸࠥࡽࡩࡵࡪࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠠࡥࡧࡷࡥ࡮ࡲࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡔ࡫ࡰ࡭ࡱࡧࡲ࡭ࡻ࠯ࠤ࡮ࡺࠠࡱࡴࡲࡧࡪࡹࡳࡦࡵࠣࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࡲ࡯ࡤࡣࡷࡩࡩࠦࡩ࡯ࠢࡋࡳࡴࡱࡌࡦࡸࡨࡰ࠴ࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠤࡧࡿࠠࡳࡧࡳࡰࡦࡩࡩ࡯ࡩࠣࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣࠢࡺ࡭ࡹ࡮ࠠࠣࡊࡲࡳࡰࡒࡥࡷࡧ࡯࠳ࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠥ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡘ࡭࡫ࠠࡤࡴࡨࡥࡹ࡫ࡤࠡࡎࡲ࡫ࡊࡴࡴࡳࡻࠣࡳࡧࡰࡥࡤࡶࡶࠤࡦࡸࡥࠡࡣࡧࡨࡪࡪࠠࡵࡱࠣࡸ࡭࡫ࠠࡩࡱࡲ࡯ࠬࡹࠠࠣ࡮ࡲ࡫ࡸࠨࠠ࡭࡫ࡶࡸ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡭ࡵ࡯࡬࠼ࠣࡘ࡭࡫ࠠࡦࡸࡨࡲࡹࠦࡤࡪࡥࡷ࡭ࡴࡴࡡࡳࡻࠣࡧࡴࡴࡴࡢ࡫ࡱ࡭ࡳ࡭ࠠࡦࡺ࡬ࡷࡹ࡯࡮ࡨࠢ࡯ࡳ࡬ࡹࠠࡢࡰࡧࠤ࡭ࡵ࡯࡬ࠢ࡬ࡲ࡫ࡵࡲ࡮ࡣࡷ࡭ࡴࡴ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡨࡰࡱ࡮ࡣࡱ࡫ࡶࡦ࡮ࡢࡪ࡮ࡲࡥࡴ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡕࡧࡴࡩࠢࡲࡦ࡯࡫ࡣࡵࡵࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩ࡚ࠥࡥࡴࡶࡏࡩࡻ࡫࡬ࠡ࡯ࡲࡲ࡮ࡺ࡯ࡳ࡫ࡱ࡫࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡧࡻࡩ࡭ࡦࡢࡰࡪࡼࡥ࡭ࡡࡩ࡭ࡱ࡫ࡳ࠻ࠢࡏ࡭ࡸࡺࠠࡰࡨࠣࡔࡦࡺࡨࠡࡱࡥ࡮ࡪࡩࡴࡴࠢࡩࡶࡴࡳࠠࡵࡪࡨࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠡ࡯ࡲࡲ࡮ࡺ࡯ࡳ࡫ࡱ࡫࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥቝ")
        global _1ll111l1ll1_opy_
        platform_index = os.environ[bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ቞")]
        bstack1ll1ll111ll_opy_ = os.path.join(bstack1ll111l1l1l_opy_, (bstack1ll1l1l1lll_opy_ + str(platform_index)), bstack1ll11l11111_opy_)
        if not os.path.exists(bstack1ll1ll111ll_opy_) or not os.path.isdir(bstack1ll1ll111ll_opy_):
            return
        logs = hook.get(bstack111111l_opy_ (u"ࠨ࡬ࡰࡩࡶࠦ቟"), [])
        with os.scandir(bstack1ll1ll111ll_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll111l1ll1_opy_:
                    self.logger.info(bstack111111l_opy_ (u"ࠢࡑࡣࡷ࡬ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡰࡳࡱࡦࡩࡸࡹࡥࡥࠢࡾࢁࠧበ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack111111l_opy_ (u"ࠣࠤቡ")
                    log_entry = bstack1ll111lll11_opy_(
                        kind=bstack111111l_opy_ (u"ࠤࡗࡉࡘ࡚࡟ࡂࡖࡗࡅࡈࡎࡍࡆࡐࡗࠦቢ"),
                        message=bstack111111l_opy_ (u"ࠥࠦባ"),
                        level=bstack111111l_opy_ (u"ࠦࠧቤ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1ll11l1ll11_opy_=entry.stat().st_size,
                        bstack1ll1l1l1l11_opy_=bstack111111l_opy_ (u"ࠧࡓࡁࡏࡗࡄࡐࡤ࡛ࡐࡍࡑࡄࡈࠧብ"),
                        bstack1111l1l_opy_=os.path.abspath(entry.path),
                        bstack1ll1l1l1ll1_opy_=hook.get(TestFramework.bstack1ll1l1111l1_opy_)
                    )
                    logs.append(log_entry)
                    _1ll111l1ll1_opy_.add(abs_path)
        platform_index = os.environ[bstack111111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ቦ")]
        bstack1ll11lll1l1_opy_ = os.path.join(bstack1ll111l1l1l_opy_, (bstack1ll1l1l1lll_opy_ + str(platform_index)), bstack1ll11l11111_opy_, bstack1ll11l1l11l_opy_)
        if not os.path.exists(bstack1ll11lll1l1_opy_) or not os.path.isdir(bstack1ll11lll1l1_opy_):
            self.logger.info(bstack111111l_opy_ (u"ࠢࡏࡱࠣࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡪࡴࡻ࡮ࡥࠢࡤࡸ࠿ࠦࡻࡾࠤቧ").format(bstack1ll11lll1l1_opy_))
        else:
            self.logger.info(bstack111111l_opy_ (u"ࠣࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡩࡶࡴࡳࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻ࠽ࠤࢀࢃࠢቨ").format(bstack1ll11lll1l1_opy_))
            with os.scandir(bstack1ll11lll1l1_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll111l1ll1_opy_:
                        self.logger.info(bstack111111l_opy_ (u"ࠤࡓࡥࡹ࡮ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤࢀࢃࠢቩ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack111111l_opy_ (u"ࠥࠦቪ")
                        log_entry = bstack1ll111lll11_opy_(
                            kind=bstack111111l_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨቫ"),
                            message=bstack111111l_opy_ (u"ࠧࠨቬ"),
                            level=bstack111111l_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠥቭ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1ll11l1ll11_opy_=entry.stat().st_size,
                            bstack1ll1l1l1l11_opy_=bstack111111l_opy_ (u"ࠢࡎࡃࡑ࡙ࡆࡒ࡟ࡖࡒࡏࡓࡆࡊࠢቮ"),
                            bstack1111l1l_opy_=os.path.abspath(entry.path),
                            bstack1ll1ll111l1_opy_=hook.get(TestFramework.bstack1ll1l1111l1_opy_)
                        )
                        logs.append(log_entry)
                        _1ll111l1ll1_opy_.add(abs_path)
        hook[bstack111111l_opy_ (u"ࠣ࡮ࡲ࡫ࡸࠨቯ")] = logs
    def bstack1ll11111111_opy_(
        self,
        bstack1ll11l11lll_opy_: bstack1lll1lll1l1_opy_,
        entries: List[bstack1ll111lll11_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack111111l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡏࡍࡤࡈࡉࡏࡡࡖࡉࡘ࡙ࡉࡐࡐࡢࡍࡉࠨተ"))
        req.platform_index = TestFramework.get_state(bstack1ll11l11lll_opy_, TestFramework.bstack1llllllll1l_opy_)
        req.execution_context.hash = str(bstack1ll11l11lll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11l11lll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11l11lll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll11l11lll_opy_, TestFramework.bstack1llll1111l1_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll11l11lll_opy_, TestFramework.bstack1llll1l11l1_opy_)
            log_entry.uuid = entry.bstack1ll1l1l1ll1_opy_ if entry.bstack1ll1l1l1ll1_opy_ else TestFramework.get_state(bstack1ll11l11lll_opy_, TestFramework.bstack1llll11lll1_opy_)
            log_entry.test_framework_state = bstack1ll11l11lll_opy_.state.name
            log_entry.message = entry.message.encode(bstack111111l_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤቱ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack111111l_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨቲ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll11l1ll11_opy_
                log_entry.file_path = entry.bstack1111l1l_opy_
        def bstack1ll1l111l11_opy_():
            bstack1111ll111_opy_ = datetime.now()
            try:
                self.bstack111111111l_opy_.LogCreatedEvent(req)
                bstack1ll11l11lll_opy_.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࡤࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠤታ"), datetime.now() - bstack1111ll111_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack111111l_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࡤࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࠢࡾࢁࠧቴ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11lllll_opy_.enqueue(bstack1ll1l111l11_opy_)
    def __1ll111ll1l1_opy_(self, instance) -> None:
        bstack111111l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡑࡵࡡࡥࡵࠣࡧࡺࡹࡴࡰ࡯ࠣࡸࡦ࡭ࡳࠡࡨࡲࡶࠥࡺࡨࡦࠢࡪ࡭ࡻ࡫࡮ࠡࡶࡨࡷࡹࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡃࡳࡧࡤࡸࡪࡹࠠࡢࠢࡧ࡭ࡨࡺࠠࡤࡱࡱࡸࡦ࡯࡮ࡪࡰࡪࠤࡹ࡫ࡳࡵࠢ࡯ࡩࡻ࡫࡬ࠡࡥࡸࡷࡹࡵ࡭ࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡶࡪࡺࡲࡪࡧࡹࡩࡩࠦࡦࡳࡱࡰࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉࡵࡴࡶࡲࡱ࡙ࡧࡧࡎࡣࡱࡥ࡬࡫ࡲࠡࡣࡱࡨࠥࡻࡰࡥࡣࡷࡩࡸࠦࡴࡩࡧࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࠥࡹࡴࡢࡶࡨࠤࡺࡹࡩ࡯ࡩࠣࡷࡪࡺ࡟ࡴࡶࡤࡸࡪࡥࡥ࡯ࡶࡵ࡭ࡪࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧት")
        bstack1ll1111ll11_opy_ = {bstack111111l_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡠ࡯ࡨࡸࡦࡪࡡࡵࡣࠥቶ"): bstack1ll1l1ll111_opy_.bstack1ll11l1lll1_opy_()}
        TestFramework.bstack1ll1l11l111_opy_(instance, bstack1ll1111ll11_opy_)
    @staticmethod
    def __1ll111lllll_opy_(instance, args):
        request, bstack1l1lllll1ll_opy_ = args
        bstack1ll111111ll_opy_ = id(bstack1l1lllll1ll_opy_)
        bstack1ll1l1l111l_opy_ = instance.data[TestFramework.bstack1ll1l1lllll_opy_]
        step = next(filter(lambda st: st[bstack111111l_opy_ (u"ࠩ࡬ࡨࠬቷ")] == bstack1ll111111ll_opy_, bstack1ll1l1l111l_opy_[bstack111111l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩቸ")]), None)
        step.update({
            bstack111111l_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨቹ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1ll1l1l111l_opy_[bstack111111l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫቺ")]) if st[bstack111111l_opy_ (u"࠭ࡩࡥࠩቻ")] == step[bstack111111l_opy_ (u"ࠧࡪࡦࠪቼ")]), None)
        if index is not None:
            bstack1ll1l1l111l_opy_[bstack111111l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧች")][index] = step
        instance.data[TestFramework.bstack1ll1l1lllll_opy_] = bstack1ll1l1l111l_opy_
    @staticmethod
    def __1ll11111ll1_opy_(instance, args):
        bstack111111l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡷࡩࡧࡱࠤࡱ࡫࡮ࠡࡣࡵ࡫ࡸࠦࡩࡴࠢ࠵࠰ࠥ࡯ࡴࠡࡵ࡬࡫ࡳ࡯ࡦࡪࡧࡶࠤࡹ࡮ࡥࡳࡧࠣ࡭ࡸࠦ࡮ࡰࠢࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡥࡷ࡭ࡳࠡࡣࡵࡩࠥ࠳ࠠ࡜ࡴࡨࡵࡺ࡫ࡳࡵ࠮ࠣࡷࡹ࡫ࡰ࡞ࠌࠣࠤࠥࠦࠠࠡࠢࠣ࡭࡫ࠦࡡࡳࡩࡶࠤࡦࡸࡥࠡ࠵ࠣࡸ࡭࡫࡮ࠡࡶ࡫ࡩࠥࡲࡡࡴࡶࠣࡺࡦࡲࡵࡦࠢ࡬ࡷࠥ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧቾ")
        bstack1ll1111l11l_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1l1lllll1ll_opy_ = args[1]
        bstack1ll111111ll_opy_ = id(bstack1l1lllll1ll_opy_)
        bstack1ll1l1l111l_opy_ = instance.data[TestFramework.bstack1ll1l1lllll_opy_]
        step = None
        if bstack1ll111111ll_opy_ is not None and bstack1ll1l1l111l_opy_.get(bstack111111l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩቿ")):
            step = next(filter(lambda st: st[bstack111111l_opy_ (u"ࠫ࡮ࡪࠧኀ")] == bstack1ll111111ll_opy_, bstack1ll1l1l111l_opy_[bstack111111l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫኁ")]), None)
            step.update({
                bstack111111l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫኂ"): bstack1ll1111l11l_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack111111l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧኃ"): bstack111111l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨኄ"),
                bstack111111l_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪኅ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack111111l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪኆ"): bstack111111l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫኇ"),
                })
        index = next((i for i, st in enumerate(bstack1ll1l1l111l_opy_[bstack111111l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫኈ")]) if st[bstack111111l_opy_ (u"࠭ࡩࡥࠩ኉")] == step[bstack111111l_opy_ (u"ࠧࡪࡦࠪኊ")]), None)
        if index is not None:
            bstack1ll1l1l111l_opy_[bstack111111l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧኋ")][index] = step
        instance.data[TestFramework.bstack1ll1l1lllll_opy_] = bstack1ll1l1l111l_opy_
    @staticmethod
    def __1l1llll1ll1_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack111111l_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫኌ")):
                examples = list(node.callspec.params[bstack111111l_opy_ (u"ࠪࡣࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡧࡻࡥࡲࡶ࡬ࡦࠩኍ")].values())
            return examples
        except:
            return []
    def bstack1l1lllll11l_opy_(self, instance: bstack1lll1lll1l1_opy_, bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_]):
        bstack1ll1111l111_opy_ = (
            PytestBDDFramework.bstack1ll11l1111l_opy_
            if bstack1lllll1l1ll_opy_[1] == bstack1lll1lll11l_opy_.PRE
            else PytestBDDFramework.bstack1ll1l111lll_opy_
        )
        hook = PytestBDDFramework.bstack1l1lllll111_opy_(instance, bstack1ll1111l111_opy_)
        entries = hook.get(TestFramework.bstack1ll11l1l1l1_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll1ll11l11_opy_, []))
        return entries
    def bstack1l1llll1lll_opy_(self, instance: bstack1lll1lll1l1_opy_, bstack1lllll1l1ll_opy_: Tuple[bstack1llll111lll_opy_, bstack1lll1lll11l_opy_]):
        bstack1ll1111l111_opy_ = (
            PytestBDDFramework.bstack1ll11l1111l_opy_
            if bstack1lllll1l1ll_opy_[1] == bstack1lll1lll11l_opy_.PRE
            else PytestBDDFramework.bstack1ll1l111lll_opy_
        )
        PytestBDDFramework.bstack1ll11ll1ll1_opy_(instance, bstack1ll1111l111_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll1ll11l11_opy_, []).clear()
    @staticmethod
    def bstack1l1lllll111_opy_(instance: bstack1lll1lll1l1_opy_, bstack1ll1111l111_opy_: str):
        bstack1ll111ll11l_opy_ = (
            PytestBDDFramework.bstack1ll111l11l1_opy_
            if bstack1ll1111l111_opy_ == PytestBDDFramework.bstack1ll1l111lll_opy_
            else PytestBDDFramework.bstack1ll1l11ll11_opy_
        )
        bstack1ll111l11ll_opy_ = TestFramework.get_state(instance, bstack1ll1111l111_opy_, None)
        bstack1ll1l111ll1_opy_ = TestFramework.get_state(instance, bstack1ll111ll11l_opy_, None) if bstack1ll111l11ll_opy_ else None
        return (
            bstack1ll1l111ll1_opy_[bstack1ll111l11ll_opy_][-1]
            if isinstance(bstack1ll1l111ll1_opy_, dict) and len(bstack1ll1l111ll1_opy_.get(bstack1ll111l11ll_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll11ll1ll1_opy_(instance: bstack1lll1lll1l1_opy_, bstack1ll1111l111_opy_: str):
        hook = PytestBDDFramework.bstack1l1lllll111_opy_(instance, bstack1ll1111l111_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll11l1l1l1_opy_, []).clear()
    @staticmethod
    def __1ll1l111l1l_opy_(instance: bstack1lll1lll1l1_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack111111l_opy_ (u"ࠦ࡬࡫ࡴࡠࡴࡨࡧࡴࡸࡤࡴࠤ኎"), None)):
            return
        if os.getenv(bstack111111l_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡑࡕࡇࡔࠤ኏"), bstack111111l_opy_ (u"ࠨ࠱ࠣነ")) != bstack111111l_opy_ (u"ࠢ࠲ࠤኑ"):
            PytestBDDFramework.logger.warning(bstack111111l_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡩ࡯ࡩࠣࡧࡦࡶ࡬ࡰࡩࠥኒ"))
            return
        bstack1ll11ll11ll_opy_ = {
            bstack111111l_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣና"): (PytestBDDFramework.bstack1ll11l1111l_opy_, PytestBDDFramework.bstack1ll1l11ll11_opy_),
            bstack111111l_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧኔ"): (PytestBDDFramework.bstack1ll1l111lll_opy_, PytestBDDFramework.bstack1ll111l11l1_opy_),
        }
        for when in (bstack111111l_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥን"), bstack111111l_opy_ (u"ࠧࡩࡡ࡭࡮ࠥኖ"), bstack111111l_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࠣኗ")):
            bstack1ll11ll111l_opy_ = args[1].get_records(when)
            if not bstack1ll11ll111l_opy_:
                continue
            records = [
                bstack1ll111lll11_opy_(
                    kind=TestFramework.bstack1ll1l1l11l1_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack111111l_opy_ (u"ࠢ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠥኘ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack111111l_opy_ (u"ࠣࡥࡵࡩࡦࡺࡥࡥࠤኙ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll11ll111l_opy_
                if isinstance(getattr(r, bstack111111l_opy_ (u"ࠤࡰࡩࡸࡹࡡࡨࡧࠥኚ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll11111lll_opy_, bstack1ll111ll11l_opy_ = bstack1ll11ll11ll_opy_.get(when, (None, None))
            bstack1ll1l11l1ll_opy_ = TestFramework.get_state(instance, bstack1ll11111lll_opy_, None) if bstack1ll11111lll_opy_ else None
            bstack1ll1l111ll1_opy_ = TestFramework.get_state(instance, bstack1ll111ll11l_opy_, None) if bstack1ll1l11l1ll_opy_ else None
            if isinstance(bstack1ll1l111ll1_opy_, dict) and len(bstack1ll1l111ll1_opy_.get(bstack1ll1l11l1ll_opy_, [])) > 0:
                hook = bstack1ll1l111ll1_opy_[bstack1ll1l11l1ll_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll11l1l1l1_opy_ in hook:
                    hook[TestFramework.bstack1ll11l1l1l1_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll1ll11l11_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll1l11llll_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        test_id = request.node.nodeid
        test_name = PytestBDDFramework.__1ll1111l1ll_opy_(request.node, scenario)
        bstack1l1llllll1l_opy_ = feature.filename
        if not test_id or not test_name or not bstack1l1llllll1l_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1llll11lll1_opy_: uuid4().__str__(),
            TestFramework.bstack1ll1l11l11l_opy_: test_id,
            TestFramework.bstack1ll11lll111_opy_: test_name,
            TestFramework.bstack1ll11ll11l1_opy_: test_id,
            TestFramework.bstack1ll11111l1l_opy_: bstack1l1llllll1l_opy_,
            TestFramework.bstack1ll11lll1ll_opy_: PytestBDDFramework.__1ll11l111l1_opy_(feature, scenario),
            TestFramework.bstack1ll1111llll_opy_: code,
            TestFramework.bstack1lll1ll1ll1_opy_: TestFramework.bstack1ll11llll1l_opy_,
            TestFramework.bstack1lll11ll1l1_opy_: test_name
        }
    @staticmethod
    def __1ll1111l1ll_opy_(node, scenario):
        if hasattr(node, bstack111111l_opy_ (u"ࠪࡧࡦࡲ࡬ࡴࡲࡨࡧࠬኛ")):
            parts = node.nodeid.rsplit(bstack111111l_opy_ (u"ࠦࡠࠨኜ"))
            params = parts[-1]
            return bstack111111l_opy_ (u"ࠧࢁࡽࠡ࡝ࡾࢁࠧኝ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1ll11l111l1_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack111111l_opy_ (u"࠭ࡴࡢࡩࡶࠫኞ")) else []) + (list(scenario.tags) if hasattr(scenario, bstack111111l_opy_ (u"ࠧࡵࡣࡪࡷࠬኟ")) else [])
    @staticmethod
    def __1ll1l111111_opy_(location):
        return bstack111111l_opy_ (u"ࠣ࠼࠽ࠦአ").join(filter(lambda x: isinstance(x, str), location))