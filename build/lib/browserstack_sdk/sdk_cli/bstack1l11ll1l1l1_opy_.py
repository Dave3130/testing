# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1ll1lll11ll_opy_ import bstack1ll1ll1111l_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll1llllll_opy_ import bstack1ll11l1l1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1lll1ll1ll1_opy_,
    bstack1lll1ll11ll_opy_,
    bstack1lll11l11ll_opy_,
    bstack1ll1l11l11l_opy_,
    bstack1l1lllll11l_opy_,
)
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from datetime import datetime, timezone
from typing import List, Dict, Any
import traceback
from bstack_utils.helper import bstack1ll1l11llll_opy_
from bstack_utils.bstack111111l1l1_opy_ import bstack1llll1l1111_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.bstack1lll11l1111_opy_ import bstack1lll111llll_opy_
from browserstack_sdk.sdk_cli.utils.bstack1ll11lll11l_opy_ import bstack1ll111l111l_opy_
from bstack_utils.bstack1ll1ll11_opy_ import bstack11llll1l_opy_
bstack1ll1111111l_opy_ = bstack1ll1l11llll_opy_()
bstack1ll1l11111l_opy_ = 1.0
bstack1l1llllllll_opy_ = bstack11l1111_opy_ (u"ࠢࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠳ࠢᖨ")
bstack11lll1l1lll_opy_ = bstack11l1111_opy_ (u"ࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦᖩ")
bstack11lll1ll111_opy_ = bstack11l1111_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨᖪ")
bstack11lll1ll1l1_opy_ = bstack11l1111_opy_ (u"ࠥࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠨᖫ")
bstack11lll1ll1ll_opy_ = bstack11l1111_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠥᖬ")
_1ll11l1l111_opy_ = set()
class bstack1l1l1111l11_opy_(TestFramework):
    bstack1ll11llllll_opy_ = bstack11l1111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࠧᖭ")
    bstack1ll111lll1l_opy_ = bstack11l1111_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࡢࡷࡹࡧࡲࡵࡧࡧࠦᖮ")
    bstack1l1lllll111_opy_ = bstack11l1111_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࡣ࡫࡯࡮ࡪࡵ࡫ࡩࡩࠨᖯ")
    bstack1ll111lll11_opy_ = bstack11l1111_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡱࡧࡳࡵࡡࡶࡸࡦࡸࡴࡦࡦࠥᖰ")
    bstack1ll1l111ll1_opy_ = bstack11l1111_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡲࡡࡴࡶࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࠧᖱ")
    bstack1ll111lllll_opy_: bool
    bstack1lll11l1111_opy_: bstack1lll111llll_opy_  = None
    bstack1llll1l1lll_opy_ = None
    bstack1ll11l1lll1_opy_ = [
        bstack1lll1ll1ll1_opy_.BEFORE_ALL,
        bstack1lll1ll1ll1_opy_.AFTER_ALL,
        bstack1lll1ll1ll1_opy_.BEFORE_EACH,
        bstack1lll1ll1ll1_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1ll111l11ll_opy_: Dict[str, str],
        bstack1ll1111l1ll_opy_: List[str]=[bstack11l1111_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥᖲ")],
        bstack1lll11l1111_opy_: bstack1lll111llll_opy_=None,
        bstack1llll1l1lll_opy_=None
    ):
        super().__init__(bstack1ll1111l1ll_opy_, bstack1ll111l11ll_opy_, bstack1lll11l1111_opy_)
        self.bstack1ll111lllll_opy_ = any(bstack11l1111_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦᖳ") in item.lower() for item in bstack1ll1111l1ll_opy_)
        self.bstack1llll1l1lll_opy_ = bstack1llll1l1lll_opy_
    def track_event(
        self,
        context: bstack1ll1l11l11l_opy_,
        test_framework_state: bstack1lll1ll1ll1_opy_,
        test_hook_state: bstack1lll11l11ll_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1lll1ll1ll1_opy_.TEST or test_framework_state in bstack1l1l1111l11_opy_.bstack1ll11l1lll1_opy_:
            bstack1ll11l1l1l1_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1lll1ll1ll1_opy_.NONE:
            self.logger.warning(bstack11l1111_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵࡩࡩࠦࡣࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡸࡪࡹࡴࡠࡪࡲࡳࡰࡥࡳࡵࡣࡷࡩࡂࠨᖴ") + str(test_hook_state) + bstack11l1111_opy_ (u"ࠨࠢᖵ"))
            return
        if not self.bstack1ll111lllll_opy_:
            self.logger.warning(bstack11l1111_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡵ࡯ࡵࡸࡴࡵࡵࡲࡵࡧࡧࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠽ࠣᖶ") + str(str(self.bstack1ll1111l1ll_opy_)) + bstack11l1111_opy_ (u"ࠣࠤᖷ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack11l1111_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱࡩࡽࡶࡥࡤࡶࡨࡨࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᖸ") + str(kwargs) + bstack11l1111_opy_ (u"ࠥࠦᖹ"))
            return
        instance = self.__1l1llll11l1_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack11l1111_opy_ (u"ࠦࡹࡸࡡࡤ࡭ࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤࡦࡸࡧࡴ࠿ࠥᖺ") + str(args) + bstack11l1111_opy_ (u"ࠧࠨᖻ"))
            return
        try:
            if instance!= None and test_framework_state in bstack1l1l1111l11_opy_.bstack1ll11l1lll1_opy_ and test_hook_state == bstack1lll11l11ll_opy_.PRE:
                bstack1l1llll111l_opy_ = bstack1llll1l1111_opy_.bstack1ll1111l111_opy_(EVENTS.bstack11l111l111_opy_.value)
                name = str(EVENTS.bstack11l111l111_opy_.name)+bstack11l1111_opy_ (u"ࠨ࠺ࠣᖼ")+str(test_framework_state.name)
                TestFramework.bstack1ll1l11lll1_opy_(instance, name, bstack1l1llll111l_opy_)
        except Exception as e:
            self.logger.debug(bstack11l1111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡨࡰࡱ࡮ࠤࡪࡸࡲࡰࡴࠣࡴࡷ࡫࠺ࠡࡽࢀࠦᖽ").format(e))
        try:
            if not TestFramework.bstack1lllllll1l1_opy_(instance, TestFramework.bstack1l1lll1l111_opy_) and test_hook_state == bstack1lll11l11ll_opy_.PRE:
                test = bstack1l1l1111l11_opy_.__1ll11111111_opy_(args[0])
                if test:
                    instance.data.update(test)
                    self.logger.debug(bstack11l1111_opy_ (u"ࠣ࡮ࡲࡥࡩ࡫ࡤࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣᖾ") + str(test_hook_state) + bstack11l1111_opy_ (u"ࠤࠥᖿ"))
            if test_framework_state == bstack1lll1ll1ll1_opy_.TEST:
                if test_hook_state == bstack1lll11l11ll_opy_.PRE and not TestFramework.bstack1lllllll1l1_opy_(instance, TestFramework.bstack1ll111ll11l_opy_):
                    TestFramework.bstack1llllll1111_opy_(instance, TestFramework.bstack1ll111ll11l_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11l1111_opy_ (u"ࠥࡷࡪࡺࠠࡵࡧࡶࡸ࠲ࡹࡴࡢࡴࡷࠤ࡫ࡵࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣᗀ") + str(test_hook_state) + bstack11l1111_opy_ (u"ࠦࠧᗁ"))
                elif test_hook_state == bstack1lll11l11ll_opy_.POST and not TestFramework.bstack1lllllll1l1_opy_(instance, TestFramework.bstack1l1lll1ll11_opy_):
                    TestFramework.bstack1llllll1111_opy_(instance, TestFramework.bstack1l1lll1ll11_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack11l1111_opy_ (u"ࠧࡹࡥࡵࠢࡷࡩࡸࡺ࠭ࡦࡰࡧࠤ࡫ࡵࡲࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࡲࡦࡨࠫ࠭ࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣᗂ") + str(test_hook_state) + bstack11l1111_opy_ (u"ࠨࠢᗃ"))
            elif test_framework_state == bstack1lll1ll1ll1_opy_.LOG and test_hook_state == bstack1lll11l11ll_opy_.POST:
                bstack1l1l1111l11_opy_.__1ll111ll1l1_opy_(instance, *args)
            elif test_framework_state == bstack1lll1ll1ll1_opy_.LOG_REPORT and test_hook_state == bstack1lll11l11ll_opy_.POST:
                self.__1ll111ll1ll_opy_(instance, *args)
                self.__1ll1l111111_opy_(instance)
            elif test_framework_state in bstack1l1l1111l11_opy_.bstack1ll11l1lll1_opy_:
                self.__1ll11l11l1l_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack11l1111_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡨࡢࡰࡧࡰࡪࡪࠠࡦࡸࡨࡲࡹࡃࡻࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠽ࠣᗄ") + str(instance.ref()) + bstack11l1111_opy_ (u"ࠣࠤᗅ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1l1llllll1l_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in bstack1l1l1111l11_opy_.bstack1ll11l1lll1_opy_ and test_hook_state == bstack1lll11l11ll_opy_.POST:
                name = str(EVENTS.bstack11l111l111_opy_.name)+bstack11l1111_opy_ (u"ࠤ࠽ࠦᗆ")+str(test_framework_state.name)
                bstack1l1llll111l_opy_ = TestFramework.bstack1ll1l1111l1_opy_(instance, name)
                bstack1llll1l1111_opy_.end(EVENTS.bstack11l111l111_opy_.value, bstack1l1llll111l_opy_+bstack11l1111_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᗇ"), bstack1l1llll111l_opy_+bstack11l1111_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᗈ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack11l1111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡭ࡵ࡯࡬ࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠧᗉ").format(e))
    def bstack1ll11ll11ll_opy_(self):
        return self.bstack1ll111lllll_opy_
    def __1l1llllll11_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack11l1111_opy_ (u"ࠨࡧࡦࡶࡢࡶࡪࡹࡵ࡭ࡶࠥᗊ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1ll1l1l1l1l_opy_(rep, [bstack11l1111_opy_ (u"ࠢࡸࡪࡨࡲࠧᗋ"), bstack11l1111_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤᗌ"), bstack11l1111_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤᗍ"), bstack11l1111_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥᗎ"), bstack11l1111_opy_ (u"ࠦࡸࡱࡩࡱࡲࡨࡨࠧᗏ"), bstack11l1111_opy_ (u"ࠧࡲ࡯࡯ࡩࡵࡩࡵࡸࡴࡦࡺࡷࠦᗐ")])
        return None
    def __1ll111ll1ll_opy_(self, instance: bstack1lll1ll11ll_opy_, *args):
        result = self.__1l1llllll11_opy_(*args)
        if not result:
            return
        failure = None
        bstack11111111ll_opy_ = None
        if result.get(bstack11l1111_opy_ (u"ࠨ࡯ࡶࡶࡦࡳࡲ࡫ࠢᗑ"), None) == bstack11l1111_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢᗒ") and len(args) > 1 and getattr(args[1], bstack11l1111_opy_ (u"ࠣࡧࡻࡧ࡮ࡴࡦࡰࠤᗓ"), None) is not None:
            failure = [{bstack11l1111_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬᗔ"): [args[1].excinfo.exconly(), result.get(bstack11l1111_opy_ (u"ࠥࡰࡴࡴࡧࡳࡧࡳࡶࡹ࡫ࡸࡵࠤᗕ"), None)]}]
            bstack11111111ll_opy_ = bstack11l1111_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧᗖ") if bstack11l1111_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣᗗ") in getattr(args[1].excinfo, bstack11l1111_opy_ (u"ࠨࡴࡺࡲࡨࡲࡦࡳࡥࠣᗘ"), bstack11l1111_opy_ (u"ࠢࠣᗙ")) else bstack11l1111_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤᗚ")
        bstack1ll11ll1l1l_opy_ = result.get(bstack11l1111_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥᗛ"), TestFramework.bstack1ll1l11l1ll_opy_)
        if bstack1ll11ll1l1l_opy_ != TestFramework.bstack1ll1l11l1ll_opy_:
            TestFramework.bstack1llllll1111_opy_(instance, TestFramework.bstack1ll1l11l1l1_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1ll111l1lll_opy_(instance, {
            TestFramework.bstack1lll11l1l1l_opy_: failure,
            TestFramework.bstack1l1lll1lll1_opy_: bstack11111111ll_opy_,
            TestFramework.bstack1lll1lll111_opy_: bstack1ll11ll1l1l_opy_,
        })
    def __1l1llll11l1_opy_(
        self,
        context: bstack1ll1l11l11l_opy_,
        test_framework_state: bstack1lll1ll1ll1_opy_,
        test_hook_state: bstack1lll11l11ll_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1lll1ll1ll1_opy_.SETUP_FIXTURE:
            instance = self.__1l1llll1lll_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1ll11l11l11_opy_ bstack1ll1111ll1l_opy_ this to be bstack11l1111_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥᗜ")
            if test_framework_state == bstack1lll1ll1ll1_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1ll1l111l1l_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1lll1ll1ll1_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack11l1111_opy_ (u"ࠦࡳࡵࡤࡦࠤᗝ"), None), bstack11l1111_opy_ (u"ࠧࡴ࡯ࡥࡧ࡬ࡨࠧᗞ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack11l1111_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨᗟ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1l1lll1l1ll_opy_(target) if target else None
        return instance
    def __1ll11l11l1l_opy_(
        self,
        instance: bstack1lll1ll11ll_opy_,
        test_framework_state: bstack1lll1ll1ll1_opy_,
        test_hook_state: bstack1lll11l11ll_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1l1lllllll1_opy_ = TestFramework.get_state(instance, bstack1l1l1111l11_opy_.bstack1ll111lll1l_opy_, {})
        if not key in bstack1l1lllllll1_opy_:
            bstack1l1lllllll1_opy_[key] = []
        bstack1ll11l11111_opy_ = TestFramework.get_state(instance, bstack1l1l1111l11_opy_.bstack1l1lllll111_opy_, {})
        if not key in bstack1ll11l11111_opy_:
            bstack1ll11l11111_opy_[key] = []
        bstack1ll1111lll1_opy_ = {
            bstack1l1l1111l11_opy_.bstack1ll111lll1l_opy_: bstack1l1lllllll1_opy_,
            bstack1l1l1111l11_opy_.bstack1l1lllll111_opy_: bstack1ll11l11111_opy_,
        }
        if test_hook_state == bstack1lll11l11ll_opy_.PRE:
            hook = {
                bstack11l1111_opy_ (u"ࠢ࡬ࡧࡼࠦᗠ"): key,
                TestFramework.bstack1ll111l1111_opy_: uuid4().__str__(),
                TestFramework.bstack1ll111l1l1l_opy_: TestFramework.bstack1ll11l1llll_opy_,
                TestFramework.bstack1ll1l1l1111_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1ll11llll11_opy_: [],
                TestFramework.bstack1ll1l1l11ll_opy_: args[1] if len(args) > 1 else bstack11l1111_opy_ (u"ࠨࠩᗡ"),
                TestFramework.bstack1ll1l1l1l11_opy_: bstack1ll111l111l_opy_.bstack1ll111llll1_opy_()
            }
            bstack1l1lllllll1_opy_[key].append(hook)
            bstack1ll1111lll1_opy_[bstack1l1l1111l11_opy_.bstack1ll111lll11_opy_] = key
        elif test_hook_state == bstack1lll11l11ll_opy_.POST:
            bstack1ll11l1l11l_opy_ = bstack1l1lllllll1_opy_.get(key, [])
            hook = bstack1ll11l1l11l_opy_.pop() if bstack1ll11l1l11l_opy_ else None
            if hook:
                result = self.__1l1llllll11_opy_(*args)
                if result:
                    bstack1l1llll11ll_opy_ = result.get(bstack11l1111_opy_ (u"ࠤࡲࡹࡹࡩ࡯࡮ࡧࠥᗢ"), TestFramework.bstack1ll11l1llll_opy_)
                    if bstack1l1llll11ll_opy_ != TestFramework.bstack1ll11l1llll_opy_:
                        hook[TestFramework.bstack1ll111l1l1l_opy_] = bstack1l1llll11ll_opy_
                hook[TestFramework.bstack1ll1l11ll11_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack1ll1l1l1l11_opy_]= bstack1ll111l111l_opy_.bstack1ll111llll1_opy_()
                self.bstack1ll1111ll11_opy_(hook)
                logs = hook.get(TestFramework.bstack1ll11lllll1_opy_, [])
                if logs: self.bstack1l1lll1ll1l_opy_(instance, logs)
                bstack1ll11l11111_opy_[key].append(hook)
                bstack1ll1111lll1_opy_[bstack1l1l1111l11_opy_.bstack1ll1l111ll1_opy_] = key
        TestFramework.bstack1ll111l1lll_opy_(instance, bstack1ll1111lll1_opy_)
        self.logger.debug(bstack11l1111_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡ࡫ࡳࡴࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾ࡯ࡪࡿࡽ࠯ࡽࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࢁࠥ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࡂࢁࡨࡰࡱ࡮ࡷࡤࡹࡴࡢࡴࡷࡩࡩࢃࠠࡩࡱࡲ࡯ࡸࡥࡦࡪࡰ࡬ࡷ࡭࡫ࡤ࠾ࠤᗣ") + str(bstack1ll11l11111_opy_) + bstack11l1111_opy_ (u"ࠦࠧᗤ"))
    def __1l1llll1lll_opy_(
        self,
        context: bstack1ll1l11l11l_opy_,
        test_framework_state: bstack1lll1ll1ll1_opy_,
        test_hook_state: bstack1lll11l11ll_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1ll1l1l1l1l_opy_(args[0], [bstack11l1111_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦᗥ"), bstack11l1111_opy_ (u"ࠨࡡࡳࡩࡱࡥࡲ࡫ࠢᗦ"), bstack11l1111_opy_ (u"ࠢࡱࡣࡵࡥࡲࡹࠢᗧ"), bstack11l1111_opy_ (u"ࠣ࡫ࡧࡷࠧᗨ"), bstack11l1111_opy_ (u"ࠤࡸࡲ࡮ࡺࡴࡦࡵࡷࠦᗩ"), bstack11l1111_opy_ (u"ࠥࡦࡦࡹࡥࡪࡦࠥᗪ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scope = request.scope if hasattr(request, bstack11l1111_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥᗫ")) else fixturedef.get(bstack11l1111_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦᗬ"), None)
        fixturename = request.fixturename if hasattr(request, bstack11l1111_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࠦᗭ")) else None
        node = request.node if hasattr(request, bstack11l1111_opy_ (u"ࠢ࡯ࡱࡧࡩࠧᗮ")) else None
        target = request.node.nodeid if hasattr(node, bstack11l1111_opy_ (u"ࠣࡰࡲࡨࡪ࡯ࡤࠣᗯ")) else None
        baseid = fixturedef.get(bstack11l1111_opy_ (u"ࠤࡥࡥࡸ࡫ࡩࡥࠤᗰ"), None) or bstack11l1111_opy_ (u"ࠥࠦᗱ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack11l1111_opy_ (u"ࠦࡤࡶࡹࡧࡷࡱࡧ࡮ࡺࡥ࡮ࠤᗲ")):
            target = bstack1l1l1111l11_opy_.__1ll111l11l1_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack11l1111_opy_ (u"ࠧࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠢᗳ")) else None
            if target and not TestFramework.bstack1l1lll1l1ll_opy_(target):
                self.__1ll1l111l1l_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack11l1111_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥࡥࡷࡧࡱࡸ࠿ࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡶࡤࡶ࡬࡫ࡴ࠾ࡽࡷࡥࡷ࡭ࡥࡵࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡰࡲࡨࡪࡃࡻ࡯ࡱࡧࡩࢂࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࠣᗴ") + str(test_hook_state) + bstack11l1111_opy_ (u"ࠢࠣᗵ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack11l1111_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠࡧࡹࡩࡳࡺ࠺ࠡࡷࡱ࡬ࡦࡴࡤ࡭ࡧࡧࠤࡪࡼࡥ࡯ࡶࡀࡿࡹ࡫ࡳࡵࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࢁ࠳ࢁࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡧࡩ࡫ࡃࡻࡧ࡫ࡻࡸࡺࡸࡥࡥࡧࡩࢁࠥࡹࡣࡰࡲࡨࡁࢀࡹࡣࡰࡲࡨࢁࠥࡺࡡࡳࡩࡨࡸࡂࠨᗶ") + str(target) + bstack11l1111_opy_ (u"ࠤࠥᗷ"))
            return None
        instance = TestFramework.bstack1l1lll1l1ll_opy_(target)
        if not instance:
            self.logger.warning(bstack11l1111_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡩ࡭ࡽࡺࡵࡳࡧࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡹࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡥࡥࡸ࡫ࡩࡥ࠿ࡾࡦࡦࡹࡥࡪࡦࢀࠤࡹࡧࡲࡨࡧࡷࡁࠧᗸ") + str(target) + bstack11l1111_opy_ (u"ࠦࠧᗹ"))
            return None
        bstack1ll11llll1l_opy_ = TestFramework.get_state(instance, bstack1l1l1111l11_opy_.bstack1ll11llllll_opy_, {})
        if os.getenv(bstack11l1111_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡋࡏࡘࡕࡗࡕࡉࡘࠨᗺ"), bstack11l1111_opy_ (u"ࠨ࠱ࠣᗻ")) == bstack11l1111_opy_ (u"ࠢ࠲ࠤᗼ"):
            bstack1ll1l1111ll_opy_ = bstack11l1111_opy_ (u"ࠣ࠼ࠥᗽ").join((scope, fixturename))
            bstack1l1llll1l1l_opy_ = datetime.now(tz=timezone.utc)
            bstack1ll11ll111l_opy_ = {
                bstack11l1111_opy_ (u"ࠤ࡮ࡩࡾࠨᗾ"): bstack1ll1l1111ll_opy_,
                bstack11l1111_opy_ (u"ࠥࡸࡦ࡭ࡳࠣᗿ"): bstack1l1l1111l11_opy_.__1ll11l1l1ll_opy_(request.node),
                bstack11l1111_opy_ (u"ࠦ࡫࡯ࡸࡵࡷࡵࡩࠧᘀ"): fixturedef,
                bstack11l1111_opy_ (u"ࠧࡹࡣࡰࡲࡨࠦᘁ"): scope,
                bstack11l1111_opy_ (u"ࠨࡴࡺࡲࡨࠦᘂ"): None,
            }
            try:
                if test_hook_state == bstack1lll11l11ll_opy_.POST and callable(getattr(args[-1], bstack11l1111_opy_ (u"ࠢࡨࡧࡷࡣࡷ࡫ࡳࡶ࡮ࡷࠦᘃ"), None)):
                    bstack1ll11ll111l_opy_[bstack11l1111_opy_ (u"ࠣࡶࡼࡴࡪࠨᘄ")] = TestFramework.bstack1ll1l1l11l1_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll11l11ll_opy_.PRE:
                bstack1ll11ll111l_opy_[bstack11l1111_opy_ (u"ࠤࡸࡹ࡮ࡪࠢᘅ")] = uuid4().__str__()
                bstack1ll11ll111l_opy_[bstack1l1l1111l11_opy_.bstack1ll1l1l1111_opy_] = bstack1l1llll1l1l_opy_
            elif test_hook_state == bstack1lll11l11ll_opy_.POST:
                bstack1ll11ll111l_opy_[bstack1l1l1111l11_opy_.bstack1ll1l11ll11_opy_] = bstack1l1llll1l1l_opy_
            if bstack1ll1l1111ll_opy_ in bstack1ll11llll1l_opy_:
                bstack1ll11llll1l_opy_[bstack1ll1l1111ll_opy_].update(bstack1ll11ll111l_opy_)
                self.logger.debug(bstack11l1111_opy_ (u"ࠥࡹࡵࡪࡡࡵࡧࡧࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡀࠦᘆ") + str(bstack1ll11llll1l_opy_[bstack1ll1l1111ll_opy_]) + bstack11l1111_opy_ (u"ࠦࠧᘇ"))
            else:
                bstack1ll11llll1l_opy_[bstack1ll1l1111ll_opy_] = bstack1ll11ll111l_opy_
                self.logger.debug(bstack11l1111_opy_ (u"ࠧࡹࡡࡷࡧࡧࠤ࡫࡯ࡸࡵࡷࡵࡩࡳࡧ࡭ࡦ࠿ࡾࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࡾࠢࡶࡧࡴࡶࡥ࠾ࡽࡶࡧࡴࡶࡥࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡀࡿࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࢀࠤࡹࡸࡡࡤ࡭ࡨࡨࡤ࡬ࡩࡹࡶࡸࡶࡪࡹ࠽ࠣᘈ") + str(len(bstack1ll11llll1l_opy_)) + bstack11l1111_opy_ (u"ࠨࠢᘉ"))
        TestFramework.bstack1llllll1111_opy_(instance, bstack1l1l1111l11_opy_.bstack1ll11llllll_opy_, bstack1ll11llll1l_opy_)
        self.logger.debug(bstack11l1111_opy_ (u"ࠢࡴࡣࡹࡩࡩࠦࡦࡪࡺࡷࡹࡷ࡫ࡳ࠾ࡽ࡯ࡩࡳ࠮ࡴࡳࡣࡦ࡯ࡪࡪ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡴࠫࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢᘊ") + str(instance.ref()) + bstack11l1111_opy_ (u"ࠣࠤᘋ"))
        return instance
    def __1ll1l111l1l_opy_(
        self,
        context: bstack1ll1l11l11l_opy_,
        test_framework_state: bstack1lll1ll1ll1_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1ll1ll1111l_opy_.create_context(target)
        ob = bstack1lll1ll11ll_opy_(ctx, self.bstack1ll1111l1ll_opy_, self.bstack1ll111l11ll_opy_, test_framework_state)
        TestFramework.bstack1ll111l1lll_opy_(ob, {
            TestFramework.bstack1lll1l1111l_opy_: context.test_framework_name,
            TestFramework.bstack1lll1l11111_opy_: context.test_framework_version,
            TestFramework.bstack1ll11l111ll_opy_: [],
            bstack1l1l1111l11_opy_.bstack1ll11llllll_opy_: {},
            bstack1l1l1111l11_opy_.bstack1l1lllll111_opy_: {},
            bstack1l1l1111l11_opy_.bstack1ll111lll1l_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1llllll1111_opy_(ob, TestFramework.bstack1l1llll1111_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1llllll1111_opy_(ob, TestFramework.bstack1llll11ll1l_opy_, context.platform_index)
        TestFramework.bstack1lll1l1llll_opy_[ctx.id] = ob
        self.logger.debug(bstack11l1111_opy_ (u"ࠤࡶࡥࡻ࡫ࡤࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠣࡧࡹࡾ࠮ࡪࡦࡀࡿࡨࡺࡸ࠯࡫ࡧࢁࠥࡺࡡࡳࡩࡨࡸࡂࢁࡴࡢࡴࡪࡩࡹࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤᘌ") + str(TestFramework.bstack1lll1l1llll_opy_.keys()) + bstack11l1111_opy_ (u"ࠥࠦᘍ"))
        return ob
    def bstack1ll1l111lll_opy_(self, instance: bstack1lll1ll11ll_opy_, bstack1llllll1lll_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll11l11ll_opy_]):
        bstack1ll111ll111_opy_ = (
            bstack1l1l1111l11_opy_.bstack1ll111lll11_opy_
            if bstack1llllll1lll_opy_[1] == bstack1lll11l11ll_opy_.PRE
            else bstack1l1l1111l11_opy_.bstack1ll1l111ll1_opy_
        )
        hook = bstack1l1l1111l11_opy_.bstack1ll111l1l11_opy_(instance, bstack1ll111ll111_opy_)
        entries = hook.get(TestFramework.bstack1ll11llll11_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.get_state(instance, TestFramework.bstack1ll11l111ll_opy_, []))
        return entries
    def bstack1ll11111ll1_opy_(self, instance: bstack1lll1ll11ll_opy_, bstack1llllll1lll_opy_: Tuple[bstack1lll1ll1ll1_opy_, bstack1lll11l11ll_opy_]):
        bstack1ll111ll111_opy_ = (
            bstack1l1l1111l11_opy_.bstack1ll111lll11_opy_
            if bstack1llllll1lll_opy_[1] == bstack1lll11l11ll_opy_.PRE
            else bstack1l1l1111l11_opy_.bstack1ll1l111ll1_opy_
        )
        bstack1l1l1111l11_opy_.bstack1ll11lll1l1_opy_(instance, bstack1ll111ll111_opy_)
        TestFramework.get_state(instance, TestFramework.bstack1ll11l111ll_opy_, []).clear()
    def bstack1ll1111ll11_opy_(self, hook: Dict[str, Any]) -> None:
        bstack11l1111_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡒࡵࡳࡨ࡫ࡳࡴࡧࡶࠤࡹ࡮ࡥࠡࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠤࡦࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴࠢࡶ࡭ࡲ࡯࡬ࡢࡴࠣࡸࡴࠦࡴࡩࡧࠣࡎࡦࡼࡡࠡ࡫ࡰࡴࡱ࡫࡭ࡦࡰࡷࡥࡹ࡯࡯࡯࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤ࡙࡮ࡩࡴࠢࡰࡩࡹ࡮࡯ࡥ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡅ࡫ࡩࡨࡱࡳࠡࡶ࡫ࡩࠥࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬ࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࡮ࡴࡳࡪࡦࡨࠤࢃ࠵࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠵ࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡋࡵࡲࠡࡧࡤࡧ࡭ࠦࡦࡪ࡮ࡨࠤ࡮ࡴࠠࡩࡱࡲ࡯ࡤࡲࡥࡷࡧ࡯ࡣ࡫࡯࡬ࡦࡵ࠯ࠤࡷ࡫ࡰ࡭ࡣࡦࡩࡸࠦࠢࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠥࠤࡼ࡯ࡴࡩࠢࠥࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠨࠠࡪࡰࠣ࡭ࡹࡹࠠࡱࡣࡷ࡬࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡎ࡬ࠠࡢࠢࡩ࡭ࡱ࡫ࠠࡪࡰࠣࡸ࡭࡫ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡱࡦࡺࡣࡩࡧࡶࠤࡦࠦ࡭ࡰࡦ࡬ࡪ࡮࡫ࡤࠡࡪࡲࡳࡰ࠳࡬ࡦࡸࡨࡰࠥ࡬ࡩ࡭ࡧ࠯ࠤ࡮ࡺࠠࡤࡴࡨࡥࡹ࡫ࡳࠡࡣࠣࡐࡴ࡭ࡅ࡯ࡶࡵࡽࠥࡵࡢ࡫ࡧࡦࡸࠥࡽࡩࡵࡪࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠠࡥࡧࡷࡥ࡮ࡲࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡔ࡫ࡰ࡭ࡱࡧࡲ࡭ࡻ࠯ࠤ࡮ࡺࠠࡱࡴࡲࡧࡪࡹࡳࡦࡵࠣࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࡲ࡯ࡤࡣࡷࡩࡩࠦࡩ࡯ࠢࡋࡳࡴࡱࡌࡦࡸࡨࡰ࠴ࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࡊࡲࡳࡰࡋࡶࡦࡰࡷࠤࡧࡿࠠࡳࡧࡳࡰࡦࡩࡩ࡯ࡩࠣࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣࠢࡺ࡭ࡹ࡮ࠠࠣࡊࡲࡳࡰࡒࡥࡷࡧ࡯࠳ࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠥ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡘ࡭࡫ࠠࡤࡴࡨࡥࡹ࡫ࡤࠡࡎࡲ࡫ࡊࡴࡴࡳࡻࠣࡳࡧࡰࡥࡤࡶࡶࠤࡦࡸࡥࠡࡣࡧࡨࡪࡪࠠࡵࡱࠣࡸ࡭࡫ࠠࡩࡱࡲ࡯ࠬࡹࠠࠣ࡮ࡲ࡫ࡸࠨࠠ࡭࡫ࡶࡸ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡭ࡵ࡯࡬࠼ࠣࡘ࡭࡫ࠠࡦࡸࡨࡲࡹࠦࡤࡪࡥࡷ࡭ࡴࡴࡡࡳࡻࠣࡧࡴࡴࡴࡢ࡫ࡱ࡭ࡳ࡭ࠠࡦࡺ࡬ࡷࡹ࡯࡮ࡨࠢ࡯ࡳ࡬ࡹࠠࡢࡰࡧࠤ࡭ࡵ࡯࡬ࠢ࡬ࡲ࡫ࡵࡲ࡮ࡣࡷ࡭ࡴࡴ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡨࡰࡱ࡮ࡣࡱ࡫ࡶࡦ࡮ࡢࡪ࡮ࡲࡥࡴ࠼ࠣࡐ࡮ࡹࡴࠡࡱࡩࠤࡕࡧࡴࡩࠢࡲࡦ࡯࡫ࡣࡵࡵࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩ࡚ࠥࡥࡴࡶࡏࡩࡻ࡫࡬ࠡ࡯ࡲࡲ࡮ࡺ࡯ࡳ࡫ࡱ࡫࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡧࡻࡩ࡭ࡦࡢࡰࡪࡼࡥ࡭ࡡࡩ࡭ࡱ࡫ࡳ࠻ࠢࡏ࡭ࡸࡺࠠࡰࡨࠣࡔࡦࡺࡨࠡࡱࡥ࡮ࡪࡩࡴࡴࠢࡩࡶࡴࡳࠠࡵࡪࡨࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠡ࡯ࡲࡲ࡮ࡺ࡯ࡳ࡫ࡱ࡫࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᘎ")
        global _1ll11l1l111_opy_
        platform_index = os.environ[bstack11l1111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬᘏ")]
        bstack1l1llll1ll1_opy_ = os.path.join(bstack1ll1111111l_opy_, (bstack1l1llllllll_opy_ + str(platform_index)), bstack11lll1ll1l1_opy_)
        if not os.path.exists(bstack1l1llll1ll1_opy_) or not os.path.isdir(bstack1l1llll1ll1_opy_):
            self.logger.debug(bstack11l1111_opy_ (u"ࠨࡄࡪࡴࡨࡧࡹࡵࡲࡺࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡪࡾࡩࡴࡶࡶࠤࡹࡵࠠࡱࡴࡲࡧࡪࡹࡳࠡࡽࢀࠦᘐ").format(bstack1l1llll1ll1_opy_))
            return
        logs = hook.get(bstack11l1111_opy_ (u"ࠢ࡭ࡱࡪࡷࠧᘑ"), [])
        with os.scandir(bstack1l1llll1ll1_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1ll11l1l111_opy_:
                    self.logger.info(bstack11l1111_opy_ (u"ࠣࡒࡤࡸ࡭ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡿࢂࠨᘒ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack11l1111_opy_ (u"ࠤࠥᘓ")
                    log_entry = bstack1l1lllll11l_opy_(
                        kind=bstack11l1111_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᘔ"),
                        message=bstack11l1111_opy_ (u"ࠦࠧᘕ"),
                        level=bstack11l1111_opy_ (u"ࠧࠨᘖ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1l1lll1llll_opy_=entry.stat().st_size,
                        bstack1ll111111l1_opy_=bstack11l1111_opy_ (u"ࠨࡍࡂࡐࡘࡅࡑࡥࡕࡑࡎࡒࡅࡉࠨᘗ"),
                        bstack1l1ll_opy_=os.path.abspath(entry.path),
                        bstack1ll11111l1l_opy_=hook.get(TestFramework.bstack1ll111l1111_opy_)
                    )
                    logs.append(log_entry)
                    _1ll11l1l111_opy_.add(abs_path)
        platform_index = os.environ[bstack11l1111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᘘ")]
        bstack1ll1l11ll1l_opy_ = os.path.join(bstack1ll1111111l_opy_, (bstack1l1llllllll_opy_ + str(platform_index)), bstack11lll1ll1l1_opy_, bstack11lll1ll1ll_opy_)
        if not os.path.exists(bstack1ll1l11ll1l_opy_) or not os.path.isdir(bstack1ll1l11ll1l_opy_):
            self.logger.info(bstack11l1111_opy_ (u"ࠣࡐࡲࠤࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࡫ࡵࡵ࡯ࡦࠣࡥࡹࡀࠠࡼࡿࠥᘙ").format(bstack1ll1l11ll1l_opy_))
        else:
            self.logger.info(bstack11l1111_opy_ (u"ࠤࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡪࡷࡵ࡭ࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼ࠾ࠥࢁࡽࠣᘚ").format(bstack1ll1l11ll1l_opy_))
            with os.scandir(bstack1ll1l11ll1l_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1ll11l1l111_opy_:
                        self.logger.info(bstack11l1111_opy_ (u"ࠥࡔࡦࡺࡨࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥࢁࡽࠣᘛ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack11l1111_opy_ (u"ࠦࠧᘜ")
                        log_entry = bstack1l1lllll11l_opy_(
                            kind=bstack11l1111_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢᘝ"),
                            message=bstack11l1111_opy_ (u"ࠨࠢᘞ"),
                            level=bstack11l1111_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦᘟ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1l1lll1llll_opy_=entry.stat().st_size,
                            bstack1ll111111l1_opy_=bstack11l1111_opy_ (u"ࠣࡏࡄࡒ࡚ࡇࡌࡠࡗࡓࡐࡔࡇࡄࠣᘠ"),
                            bstack1l1ll_opy_=os.path.abspath(entry.path),
                            bstack1ll11l1ll11_opy_=hook.get(TestFramework.bstack1ll111l1111_opy_)
                        )
                        logs.append(log_entry)
                        _1ll11l1l111_opy_.add(abs_path)
        hook[bstack11l1111_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢᘡ")] = logs
    def bstack1l1lll1ll1l_opy_(
        self,
        bstack1ll11ll1lll_opy_: bstack1lll1ll11ll_opy_,
        entries: List[bstack1l1lllll11l_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack11l1111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡗࡊ࡙ࡓࡊࡑࡑࡣࡎࡊࠢᘢ"))
        req.platform_index = TestFramework.get_state(bstack1ll11ll1lll_opy_, TestFramework.bstack1llll11ll1l_opy_)
        req.execution_context.hash = str(bstack1ll11ll1lll_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll11ll1lll_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll11ll1lll_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll11ll1lll_opy_, TestFramework.bstack1lll1l1111l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll11ll1lll_opy_, TestFramework.bstack1lll1l11111_opy_)
            log_entry.uuid = entry.bstack1ll11111l1l_opy_
            log_entry.test_framework_state = bstack1ll11ll1lll_opy_.state.name
            log_entry.message = entry.message.encode(bstack11l1111_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᘣ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            log_entry.level = bstack11l1111_opy_ (u"ࠧࠨᘤ")
            if entry.kind == bstack11l1111_opy_ (u"ࠨࡔࡆࡕࡗࡣࡆ࡚ࡔࡂࡅࡋࡑࡊࡔࡔࠣᘥ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1l1lll1llll_opy_
                log_entry.file_path = entry.bstack1l1ll_opy_
        def bstack1ll1l11l111_opy_():
            bstack11ll111l1_opy_ = datetime.now()
            try:
                self.bstack1llll1l1lll_opy_.LogCreatedEvent(req)
                bstack1ll11ll1lll_opy_.bstack1ll1l11l1_opy_(bstack11l1111_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺ࡟ࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠦᘦ"), datetime.now() - bstack11ll111l1_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11l1111_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺ࡟ࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠤࢀࢃࠢᘧ").format(str(e)))
                traceback.print_exc()
        self.bstack1lll11l1111_opy_.enqueue(bstack1ll1l11l111_opy_)
    def __1ll1l111111_opy_(self, instance) -> None:
        bstack11l1111_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡌࡰࡣࡧࡷࠥࡩࡵࡴࡶࡲࡱࠥࡺࡡࡨࡵࠣࡪࡴࡸࠠࡵࡪࡨࠤ࡬࡯ࡶࡦࡰࠣࡸࡪࡹࡴࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡅࡵࡩࡦࡺࡥࡴࠢࡤࠤࡩ࡯ࡣࡵࠢࡦࡳࡳࡺࡡࡪࡰ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡱ࡫ࡶࡦ࡮ࠣࡧࡺࡹࡴࡰ࡯ࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࡤࠡࡨࡵࡳࡲࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡷࡶࡸࡴࡳࡔࡢࡩࡐࡥࡳࡧࡧࡦࡴࠣࡥࡳࡪࠠࡶࡲࡧࡥࡹ࡫ࡳࠡࡶ࡫ࡩࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠠࡴࡶࡤࡸࡪࠦࡵࡴ࡫ࡱ࡫ࠥࡹࡥࡵࡡࡶࡸࡦࡺࡥࡠࡧࡱࡸࡷ࡯ࡥࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᘨ")
        bstack1ll1111lll1_opy_ = {bstack11l1111_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯ࡢࡱࡪࡺࡡࡥࡣࡷࡥࠧᘩ"): bstack1ll111l111l_opy_.bstack1ll111llll1_opy_()}
        from browserstack_sdk.sdk_cli.test_framework import TestFramework
        TestFramework.bstack1ll111l1lll_opy_(instance, bstack1ll1111lll1_opy_)
    @staticmethod
    def bstack1ll111l1l11_opy_(instance: bstack1lll1ll11ll_opy_, bstack1ll111ll111_opy_: str):
        bstack1ll11111l11_opy_ = (
            bstack1l1l1111l11_opy_.bstack1l1lllll111_opy_
            if bstack1ll111ll111_opy_ == bstack1l1l1111l11_opy_.bstack1ll1l111ll1_opy_
            else bstack1l1l1111l11_opy_.bstack1ll111lll1l_opy_
        )
        bstack1ll11ll1111_opy_ = TestFramework.get_state(instance, bstack1ll111ll111_opy_, None)
        bstack1ll11l1111l_opy_ = TestFramework.get_state(instance, bstack1ll11111l11_opy_, None) if bstack1ll11ll1111_opy_ else None
        return (
            bstack1ll11l1111l_opy_[bstack1ll11ll1111_opy_][-1]
            if isinstance(bstack1ll11l1111l_opy_, dict) and len(bstack1ll11l1111l_opy_.get(bstack1ll11ll1111_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1ll11lll1l1_opy_(instance: bstack1lll1ll11ll_opy_, bstack1ll111ll111_opy_: str):
        hook = bstack1l1l1111l11_opy_.bstack1ll111l1l11_opy_(instance, bstack1ll111ll111_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1ll11llll11_opy_, []).clear()
    @staticmethod
    def __1ll111ll1l1_opy_(instance: bstack1lll1ll11ll_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack11l1111_opy_ (u"ࠦ࡬࡫ࡴࡠࡴࡨࡧࡴࡸࡤࡴࠤᘪ"), None)):
            return
        if os.getenv(bstack11l1111_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡑࡕࡇࡔࠤᘫ"), bstack11l1111_opy_ (u"ࠨ࠱ࠣᘬ")) != bstack11l1111_opy_ (u"ࠢ࠲ࠤᘭ"):
            bstack1l1l1111l11_opy_.logger.warning(bstack11l1111_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡩ࡯ࡩࠣࡧࡦࡶ࡬ࡰࡩࠥᘮ"))
            return
        bstack1ll1111llll_opy_ = {
            bstack11l1111_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣᘯ"): (bstack1l1l1111l11_opy_.bstack1ll111lll11_opy_, bstack1l1l1111l11_opy_.bstack1ll111lll1l_opy_),
            bstack11l1111_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧᘰ"): (bstack1l1l1111l11_opy_.bstack1ll1l111ll1_opy_, bstack1l1l1111l11_opy_.bstack1l1lllll111_opy_),
        }
        for when in (bstack11l1111_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥᘱ"), bstack11l1111_opy_ (u"ࠧࡩࡡ࡭࡮ࠥᘲ"), bstack11l1111_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࠣᘳ")):
            bstack1ll11111lll_opy_ = args[1].get_records(when)
            if not bstack1ll11111lll_opy_:
                continue
            records = [
                bstack1l1lllll11l_opy_(
                    kind=TestFramework.bstack1ll11ll1ll1_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack11l1111_opy_ (u"ࠢ࡭ࡧࡹࡩࡱࡴࡡ࡮ࡧࠥᘴ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack11l1111_opy_ (u"ࠣࡥࡵࡩࡦࡺࡥࡥࠤᘵ")) and r.created
                        else None
                    ),
                )
                for r in bstack1ll11111lll_opy_
                if isinstance(getattr(r, bstack11l1111_opy_ (u"ࠤࡰࡩࡸࡹࡡࡨࡧࠥᘶ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1ll111l1ll1_opy_, bstack1ll11111l11_opy_ = bstack1ll1111llll_opy_.get(when, (None, None))
            bstack1ll11l11lll_opy_ = TestFramework.get_state(instance, bstack1ll111l1ll1_opy_, None) if bstack1ll111l1ll1_opy_ else None
            bstack1ll11l1111l_opy_ = TestFramework.get_state(instance, bstack1ll11111l11_opy_, None) if bstack1ll11l11lll_opy_ else None
            if isinstance(bstack1ll11l1111l_opy_, dict) and len(bstack1ll11l1111l_opy_.get(bstack1ll11l11lll_opy_, [])) > 0:
                hook = bstack1ll11l1111l_opy_[bstack1ll11l11lll_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1ll11llll11_opy_ in hook:
                    hook[TestFramework.bstack1ll11llll11_opy_].extend(records)
                    continue
            logs = TestFramework.get_state(instance, TestFramework.bstack1ll11l111ll_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1ll11111111_opy_(test) -> Dict[str, Any]:
        test_id = bstack1l1l1111l11_opy_.__1ll111l11l1_opy_(test.location) if hasattr(test, bstack11l1111_opy_ (u"ࠥࡰࡴࡩࡡࡵ࡫ࡲࡲࠧᘷ")) else getattr(test, bstack11l1111_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᘸ"), None)
        test_name = test.name if hasattr(test, bstack11l1111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᘹ")) else None
        bstack1ll11l1ll1l_opy_ = test.fspath.strpath if hasattr(test, bstack11l1111_opy_ (u"ࠨࡦࡴࡲࡤࡸ࡭ࠨᘺ")) and test.fspath else None
        if not test_id or not test_name or not bstack1ll11l1ll1l_opy_:
            return None
        code = None
        if hasattr(test, bstack11l1111_opy_ (u"ࠢࡰࡤ࡭ࠦᘻ")):
            try:
                import inspect
                code = inspect.getsource(test.obj)
            except:
                pass
        bstack11lll1ll11l_opy_ = []
        try:
            bstack11lll1ll11l_opy_ = bstack11llll1l_opy_.bstack1lll1ll1_opy_(test)
        except:
            bstack1l1l1111l11_opy_.logger.warning(bstack11l1111_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡷࡩࡸࡺࠠࡴࡥࡲࡴࡪࡹࠬࠡࡶࡨࡷࡹࠦࡳࡤࡱࡳࡩࡸࠦࡷࡪ࡮࡯ࠤࡧ࡫ࠠࡳࡧࡶࡳࡱࡼࡥࡥࠢ࡬ࡲࠥࡉࡌࡊࠤᘼ"))
        return {
            TestFramework.bstack1lll11ll111_opy_: uuid4().__str__(),
            TestFramework.bstack1l1lll1l111_opy_: test_id,
            TestFramework.bstack1l1lll11lll_opy_: test_name,
            TestFramework.bstack1l1lllll1ll_opy_: getattr(test, bstack11l1111_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᘽ"), None),
            TestFramework.bstack1l1llll1l11_opy_: bstack1ll11l1ll1l_opy_,
            TestFramework.bstack1ll11l111l1_opy_: bstack1l1l1111l11_opy_.__1ll11l1l1ll_opy_(test),
            TestFramework.bstack1ll1111l11l_opy_: code,
            TestFramework.bstack1lll1lll111_opy_: TestFramework.bstack1ll1l11l1ll_opy_,
            TestFramework.bstack1lll111lll1_opy_: test_id,
            TestFramework.bstack1l1111111l1_opy_: bstack11lll1ll11l_opy_
        }
    @staticmethod
    def __1ll11l1l1ll_opy_(test) -> List[str]:
        markers = []
        current = test
        while current:
            own_markers = getattr(current, bstack11l1111_opy_ (u"ࠥࡳࡼࡴ࡟࡮ࡣࡵ࡯ࡪࡸࡳࠣᘾ"), [])
            markers.extend([getattr(m, bstack11l1111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᘿ"), None) for m in own_markers if getattr(m, bstack11l1111_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᙀ"), None)])
            current = getattr(current, bstack11l1111_opy_ (u"ࠨࡰࡢࡴࡨࡲࡹࠨᙁ"), None)
        return markers
    @staticmethod
    def __1ll111l11l1_opy_(location):
        return bstack11l1111_opy_ (u"ࠢ࠻࠼ࠥᙂ").join(filter(lambda x: isinstance(x, str), location))