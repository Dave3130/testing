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
from datetime import datetime, timezone
import os
import builtins
from pathlib import Path
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1lllll11ll1_opy_ import bstack1llllllll1l_opy_, bstack1lllll11l1l_opy_, bstack1111111lll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1lll11_opy_ import bstack1llll1lll1l_opy_
from browserstack_sdk.sdk_cli.bstack1lll111l1ll_opy_ import bstack1lll11l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1lllllll111_opy_ import bstack1lllll11l11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11l1ll_opy_, bstack1lll1l1l1ll_opy_, bstack1lll1llll11_opy_, bstack1ll11lll111_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1lll1llll1l_opy_, bstack1ll1l11ll11_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1l11ll1l11l_opy_ = [bstack1ll1l_opy_ (u"ࠣࡰࡤࡱࡪࠨᎪ"), bstack1ll1l_opy_ (u"ࠤࡳࡥࡷ࡫࡮ࡵࠤᎫ"), bstack1ll1l_opy_ (u"ࠥࡧࡴࡴࡦࡪࡩࠥᎬ"), bstack1ll1l_opy_ (u"ࠦࡸ࡫ࡳࡴ࡫ࡲࡲࠧᎭ"), bstack1ll1l_opy_ (u"ࠧࡶࡡࡵࡪࠥᎮ")]
bstack1ll1111llll_opy_ = bstack1ll1l11ll11_opy_()
bstack1ll1l11lll1_opy_ = bstack1ll1l_opy_ (u"ࠨࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠲ࠨᎯ")
bstack1l11l111ll1_opy_ = {
    bstack1ll1l_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡱࡻࡷ࡬ࡴࡴ࠮ࡊࡶࡨࡱࠧᎰ"): bstack1l11ll1l11l_opy_,
    bstack1ll1l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯ࡲࡼࡸ࡭ࡵ࡮࠯ࡒࡤࡧࡰࡧࡧࡦࠤᎱ"): bstack1l11ll1l11l_opy_,
    bstack1ll1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡳࡽࡹ࡮࡯࡯࠰ࡐࡳࡩࡻ࡬ࡦࠤᎲ"): bstack1l11ll1l11l_opy_,
    bstack1ll1l_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡴࡾࡺࡨࡰࡰ࠱ࡇࡱࡧࡳࡴࠤᎳ"): bstack1l11ll1l11l_opy_,
    bstack1ll1l_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡵࡿࡴࡩࡱࡱ࠲ࡋࡻ࡮ࡤࡶ࡬ࡳࡳࠨᎴ"): bstack1l11ll1l11l_opy_
    + [
        bstack1ll1l_opy_ (u"ࠧࡵࡲࡪࡩ࡬ࡲࡦࡲ࡮ࡢ࡯ࡨࠦᎵ"),
        bstack1ll1l_opy_ (u"ࠨ࡫ࡦࡻࡺࡳࡷࡪࡳࠣᎶ"),
        bstack1ll1l_opy_ (u"ࠢࡧ࡫ࡻࡸࡺࡸࡥࡪࡰࡩࡳࠧᎷ"),
        bstack1ll1l_opy_ (u"ࠣ࡭ࡨࡽࡼࡵࡲࡥࡵࠥᎸ"),
        bstack1ll1l_opy_ (u"ࠤࡦࡥࡱࡲࡳࡱࡧࡦࠦᎹ"),
        bstack1ll1l_opy_ (u"ࠥࡧࡦࡲ࡬ࡰࡤ࡭ࠦᎺ"),
        bstack1ll1l_opy_ (u"ࠦࡸࡺࡡࡳࡶࠥᎻ"),
        bstack1ll1l_opy_ (u"ࠧࡹࡴࡰࡲࠥᎼ"),
        bstack1ll1l_opy_ (u"ࠨࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠣᎽ"),
        bstack1ll1l_opy_ (u"ࠢࡸࡪࡨࡲࠧᎾ"),
    ],
    bstack1ll1l_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯࡯ࡤ࡭ࡳ࠴ࡓࡦࡵࡶ࡭ࡴࡴࠢᎿ"): [bstack1ll1l_opy_ (u"ࠤࡶࡸࡦࡸࡴࡱࡣࡷ࡬ࠧᏀ"), bstack1ll1l_opy_ (u"ࠥࡸࡪࡹࡴࡴࡨࡤ࡭ࡱ࡫ࡤࠣᏁ"), bstack1ll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡵࡦࡳࡱࡲࡥࡤࡶࡨࡨࠧᏂ"), bstack1ll1l_opy_ (u"ࠧ࡯ࡴࡦ࡯ࡶࠦᏃ")],
    bstack1ll1l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡣࡰࡰࡩ࡭࡬࠴ࡃࡰࡰࡩ࡭࡬ࠨᏄ"): [bstack1ll1l_opy_ (u"ࠢࡪࡰࡹࡳࡨࡧࡴࡪࡱࡱࡣࡵࡧࡲࡢ࡯ࡶࠦᏅ"), bstack1ll1l_opy_ (u"ࠣࡣࡵ࡫ࡸࠨᏆ")],
    bstack1ll1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡩ࡭ࡽࡺࡵࡳࡧࡶ࠲ࡋ࡯ࡸࡵࡷࡵࡩࡉ࡫ࡦࠣᏇ"): [bstack1ll1l_opy_ (u"ࠥࡷࡨࡵࡰࡦࠤᏈ"), bstack1ll1l_opy_ (u"ࠦࡦࡸࡧ࡯ࡣࡰࡩࠧᏉ"), bstack1ll1l_opy_ (u"ࠧ࡬ࡵ࡯ࡥࠥᏊ"), bstack1ll1l_opy_ (u"ࠨࡰࡢࡴࡤࡱࡸࠨᏋ"), bstack1ll1l_opy_ (u"ࠢࡶࡰ࡬ࡸࡹ࡫ࡳࡵࠤᏌ"), bstack1ll1l_opy_ (u"ࠣ࡫ࡧࡷࠧᏍ")],
    bstack1ll1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡩ࡭ࡽࡺࡵࡳࡧࡶ࠲ࡘࡻࡢࡓࡧࡴࡹࡪࡹࡴࠣᏎ"): [bstack1ll1l_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥࠣᏏ"), bstack1ll1l_opy_ (u"ࠦࡵࡧࡲࡢ࡯ࠥᏐ"), bstack1ll1l_opy_ (u"ࠧࡶࡡࡳࡣࡰࡣ࡮ࡴࡤࡦࡺࠥᏑ")],
    bstack1ll1l_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡲࡶࡰࡱࡩࡷ࠴ࡃࡢ࡮࡯ࡍࡳ࡬࡯ࠣᏒ"): [bstack1ll1l_opy_ (u"ࠢࡸࡪࡨࡲࠧᏓ"), bstack1ll1l_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࠣᏔ")],
    bstack1ll1l_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡰࡥࡷࡱ࠮ࡴࡶࡵࡹࡨࡺࡵࡳࡧࡶ࠲ࡓࡵࡤࡦࡍࡨࡽࡼࡵࡲࡥࡵࠥᏕ"): [bstack1ll1l_opy_ (u"ࠥࡲࡴࡪࡥࠣᏖ"), bstack1ll1l_opy_ (u"ࠦࡵࡧࡲࡦࡰࡷࠦᏗ")],
    bstack1ll1l_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡳࡡࡳ࡭࠱ࡷࡹࡸࡵࡤࡶࡸࡶࡪࡹ࠮ࡎࡣࡵ࡯ࠧᏘ"): [bstack1ll1l_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᏙ"), bstack1ll1l_opy_ (u"ࠢࡢࡴࡪࡷࠧᏚ"), bstack1ll1l_opy_ (u"ࠣ࡭ࡺࡥࡷ࡭ࡳࠣᏛ")],
}
_1ll11l11111_opy_ = set()
class bstack1l1l11l1lll_opy_(bstack1llll1lll1l_opy_):
    bstack1l11l11lll1_opy_ = bstack1ll1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡥࡧࡩࡩࡷࡸࡥࡥࠤᏜ")
    bstack1l11l1l1l1l_opy_ = bstack1ll1l_opy_ (u"ࠥࡍࡓࡌࡏࠣᏝ")
    bstack1l11l1l111l_opy_ = bstack1ll1l_opy_ (u"ࠦࡊࡘࡒࡐࡔࠥᏞ")
    bstack1l11l11ll1l_opy_: Callable
    bstack1l11l11l111_opy_: Callable
    def __init__(self, bstack1l1l1ll1lll_opy_, bstack1ll1lllll11_opy_):
        super().__init__()
        self.bstack1l111llllll_opy_ = bstack1ll1lllll11_opy_
        if os.getenv(bstack1ll1l_opy_ (u"࡙ࠧࡄࡌࡡࡆࡐࡎࡥࡆࡍࡃࡊࡣࡔ࠷࠱࡚ࠤᏟ"), bstack1ll1l_opy_ (u"ࠨ࠱ࠣᏠ")) != bstack1ll1l_opy_ (u"ࠢ࠲ࠤᏡ") or not self.is_enabled():
            self.logger.warning(bstack1ll1l_opy_ (u"ࠣࠤᏢ") + str(self.__class__.__name__) + bstack1ll1l_opy_ (u"ࠤࠣࡨ࡮ࡹࡡࡣ࡮ࡨࡨࠧᏣ"))
            return
        TestFramework.bstack1lllll1l11l_opy_((bstack1llll11l1ll_opy_.TEST, bstack1lll1llll11_opy_.PRE), self.bstack1llll11111l_opy_)
        TestFramework.bstack1lllll1l11l_opy_((bstack1llll11l1ll_opy_.TEST, bstack1lll1llll11_opy_.POST), self.bstack1llll11l111_opy_)
        for event in bstack1llll11l1ll_opy_:
            for state in bstack1lll1llll11_opy_:
                TestFramework.bstack1lllll1l11l_opy_((event, state), self.bstack1l11ll1l1l1_opy_)
        bstack1l1l1ll1lll_opy_.bstack1lllll1l11l_opy_((bstack1lllll11l1l_opy_.bstack1111111111_opy_, bstack1111111lll_opy_.POST), self.bstack1l11l111111_opy_)
        self.bstack1l11l11ll1l_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l11ll111l1_opy_(bstack1l1l11l1lll_opy_.bstack1l11l1l1l1l_opy_, self.bstack1l11l11ll1l_opy_)
        self.bstack1l11l11l111_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l11ll111l1_opy_(bstack1l1l11l1lll_opy_.bstack1l11l1l111l_opy_, self.bstack1l11l11l111_opy_)
        self.bstack1l11ll1l1ll_opy_ = builtins.print
        builtins.print = self.bstack1l11ll11l11_opy_()
    def is_enabled(self) -> bool:
        return True
    def bstack1l11ll1l1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1ll11lll1ll_opy_() and instance:
            bstack1l11l11ll11_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1llllll111l_opy_
            if test_framework_state == bstack1llll11l1ll_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1llll11l1ll_opy_.LOG:
                bstack1l11l11lll_opy_ = datetime.now()
                entries = f.bstack1ll1l111l1l_opy_(instance, bstack1llllll111l_opy_)
                if entries:
                    self.bstack1ll1l1ll111_opy_(instance, entries)
                    instance.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࠥᏤ"), datetime.now() - bstack1l11l11lll_opy_)
                    f.bstack1ll11l1lll1_opy_(instance, bstack1llllll111l_opy_)
                instance.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠦࡴ࠷࠱ࡺ࠼ࡲࡲࡤࡧ࡬࡭ࡡࡷࡩࡸࡺ࡟ࡦࡸࡨࡲࡹࡹࠢᏥ"), datetime.now() - bstack1l11l11ll11_opy_)
                return # do not send this event with the bstack1l11l11l1l1_opy_ bstack1l11l1l1111_opy_
            elif (
                test_framework_state == bstack1llll11l1ll_opy_.TEST
                and test_hook_state == bstack1lll1llll11_opy_.POST
                and not f.bstack1lllll11lll_opy_(instance, TestFramework.bstack1l1llllll1l_opy_)
            ):
                self.logger.warning(bstack1ll1l_opy_ (u"ࠧࡪࡲࡰࡲࡳ࡭ࡳ࡭ࠠࡥࡷࡨࠤࡹࡵࠠ࡭ࡣࡦ࡯ࠥࡵࡦࠡࡴࡨࡷࡺࡲࡴࡴࠢࠥᏦ") + str(TestFramework.bstack1lllll11lll_opy_(instance, TestFramework.bstack1l1llllll1l_opy_)) + bstack1ll1l_opy_ (u"ࠨࠢᏧ"))
                f.bstack1111111ll1_opy_(instance, bstack1l1l11l1lll_opy_.bstack1l11l11lll1_opy_, True)
                return # do not send this event bstack1l11ll11l1l_opy_ bstack1l11l11111l_opy_
            elif (
                f.get_state(instance, bstack1l1l11l1lll_opy_.bstack1l11l11lll1_opy_, False)
                and test_framework_state == bstack1llll11l1ll_opy_.LOG_REPORT
                and test_hook_state == bstack1lll1llll11_opy_.POST
                and f.bstack1lllll11lll_opy_(instance, TestFramework.bstack1l1llllll1l_opy_)
            ):
                self.logger.warning(bstack1ll1l_opy_ (u"ࠢࡪࡰ࡭ࡩࡨࡺࡩ࡯ࡩࠣࡘࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡖࡸࡦࡺࡥ࠯ࡖࡈࡗ࡙࠲ࠠࡕࡧࡶࡸࡍࡵ࡯࡬ࡕࡷࡥࡹ࡫࠮ࡑࡑࡖࡘࠥࠨᏨ") + str(TestFramework.bstack1lllll11lll_opy_(instance, TestFramework.bstack1l1llllll1l_opy_)) + bstack1ll1l_opy_ (u"ࠣࠤᏩ"))
                self.bstack1l11ll1l1l1_opy_(f, instance, (bstack1llll11l1ll_opy_.TEST, bstack1lll1llll11_opy_.POST), *args, **kwargs)
            bstack1l11l11lll_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l11l111lll_opy_ = sorted(
                filter(lambda x: x.get(bstack1ll1l_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠧᏪ"), None), data.pop(bstack1ll1l_opy_ (u"ࠥࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡵࠥᏫ"), {}).values()),
                key=lambda x: x[bstack1ll1l_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠢᏬ")],
            )
            if bstack1lll11l1ll1_opy_.bstack1llll1l11l1_opy_ in data:
                data.pop(bstack1lll11l1ll1_opy_.bstack1llll1l11l1_opy_)
            data.update({bstack1ll1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪ࡮ࡾࡴࡶࡴࡨࡷࠧᏭ"): bstack1l11l111lll_opy_})
            instance.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠨࡪࡴࡱࡱ࠾ࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࠦᏮ"), datetime.now() - bstack1l11l11lll_opy_)
            bstack1l11l11lll_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l11l1111l1_opy_)
            instance.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠢ࡫ࡵࡲࡲ࠿ࡵ࡮ࡠࡣ࡯ࡰࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵࡵࠥᏯ"), datetime.now() - bstack1l11l11lll_opy_)
            self.bstack1l11l1l1111_opy_(instance, bstack1llllll111l_opy_, event_json=event_json)
            instance.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠣࡱ࠴࠵ࡾࡀ࡯࡯ࡡࡤࡰࡱࡥࡴࡦࡵࡷࡣࡪࡼࡥ࡯ࡶࡶࠦᏰ"), datetime.now() - bstack1l11l11ll11_opy_)
    def bstack1llll11111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack111l11llll_opy_ import bstack1llll1l1l11_opy_
        bstack1l1lllll111_opy_ = bstack1llll1l1l11_opy_.bstack1ll1ll1111l_opy_(EVENTS.bstack111l11ll11_opy_.value)
        self.bstack1l111llllll_opy_.bstack1lll1lll1ll_opy_(instance, f, bstack1llllll111l_opy_, *args, **kwargs)
        bstack1llll1l1l11_opy_.end(EVENTS.bstack111l11ll11_opy_.value, bstack1l1lllll111_opy_ + bstack1ll1l_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᏱ"), bstack1l1lllll111_opy_ + bstack1ll1l_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᏲ"), status=True, failure=None, test_name=None)
    def bstack1llll11l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1l111llllll_opy_.bstack1lll1l1l111_opy_(instance, f, bstack1llllll111l_opy_, *args, **kwargs)
        self.bstack1l11l11llll_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1l11l1lllll_opy_, stage=STAGE.bstack11lll11ll_opy_)
    def bstack1l11l11llll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1l1ll_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡘࡱࡩࡱࡲ࡬ࡲ࡬ࠦࡔࡦࡵࡷࡗࡪࡹࡳࡪࡱࡱࡉࡻ࡫࡮ࡵࠢࡪࡖࡕࡉࠠࡤࡣ࡯ࡰ࠿ࠦࡎࡰࠢࡹࡥࡱ࡯ࡤࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡧࡥࡹࡧࠢᏳ"))
            return
        bstack1l11l11lll_opy_ = datetime.now()
        try:
            r = self.bstack1llll1l1ll1_opy_.TestSessionEvent(req)
            instance.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠࡶࡨࡷࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡦࡸࡨࡲࡹࠨᏴ"), datetime.now() - bstack1l11l11lll_opy_)
            f.bstack1111111ll1_opy_(instance, self.bstack1l111llllll_opy_.bstack1llll11ll11_opy_, r.success)
            if not r.success:
                self.logger.info(bstack1ll1l_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣᏵ") + str(r) + bstack1ll1l_opy_ (u"ࠢࠣ᏶"))
        except grpc.RpcError as e:
            self.logger.error(bstack1ll1l_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨ᏷") + str(e) + bstack1ll1l_opy_ (u"ࠤࠥᏸ"))
            traceback.print_exc()
            raise e
    def bstack1l11l111111_opy_(
        self,
        f: bstack1lllll11l11_opy_,
        _driver: object,
        exec: Tuple[bstack1llllllll1l_opy_, str],
        _1l11l11l1ll_opy_: Tuple[bstack1lllll11l1l_opy_, bstack1111111lll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1lllll11l11_opy_.bstack1l1lll1l1ll_opy_(method_name):
            return
        if f.bstack1l1lll1l11l_opy_(*args) == bstack1lllll11l11_opy_.bstack1l11ll11ll1_opy_:
            bstack1l11l11ll11_opy_ = datetime.now()
            screenshot = result.get(bstack1ll1l_opy_ (u"ࠥࡺࡦࡲࡵࡦࠤᏹ"), None) if isinstance(result, dict) else None
            if not isinstance(screenshot, str) or len(screenshot) <= 0:
                self.logger.warning(bstack1ll1l_opy_ (u"ࠦ࡮ࡴࡶࡢ࡮࡬ࡨࠥࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠢ࡬ࡱࡦ࡭ࡥࠡࡤࡤࡷࡪ࠼࠴ࠡࡵࡷࡶࠧᏺ"))
                return
            bstack1ll1111111l_opy_ = self.bstack1l11l1ll1l1_opy_(instance)
            if bstack1ll1111111l_opy_:
                entry = bstack1ll11lll111_opy_(TestFramework.bstack1l11ll1111l_opy_, screenshot)
                self.bstack1ll1l1ll111_opy_(bstack1ll1111111l_opy_, [entry])
                instance.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠧࡵ࠱࠲ࡻ࠽ࡳࡳࡥࡡࡧࡶࡨࡶࡤ࡫ࡸࡦࡥࡸࡸࡪࠨᏻ"), datetime.now() - bstack1l11l11ll11_opy_)
            else:
                self.logger.warning(bstack1ll1l_opy_ (u"ࠨࡵ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥࡺࡥࡴࡶࠣࡪࡴࡸࠠࡸࡪ࡬ࡧ࡭ࠦࡴࡩ࡫ࡶࠤࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠡࡹࡤࡷࠥࡺࡡ࡬ࡧࡱࠤࡧࡿࠠࡥࡴ࡬ࡺࡪࡸ࠽ࠡࡽࢀࠦᏼ").format(instance.ref()))
        event = {}
        bstack1ll1111111l_opy_ = self.bstack1l11l1ll1l1_opy_(instance)
        if bstack1ll1111111l_opy_:
            self.bstack1l11l1l11l1_opy_(event, bstack1ll1111111l_opy_)
            if event.get(bstack1ll1l_opy_ (u"ࠢ࡭ࡱࡪࡷࠧᏽ")):
                self.bstack1ll1l1ll111_opy_(bstack1ll1111111l_opy_, event[bstack1ll1l_opy_ (u"ࠣ࡮ࡲ࡫ࡸࠨ᏾")])
            else:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡ࡮ࡲ࡫ࡸࠦࡦࡰࡴࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࠠࡦࡸࡨࡲࡹࠨ᏿"))
    @measure(event_name=EVENTS.bstack1l11ll1l111_opy_, stage=STAGE.bstack11lll11ll_opy_)
    def bstack1ll1l1ll111_opy_(
        self,
        bstack1ll1111111l_opy_: bstack1lll1l1l1ll_opy_,
        entries: List[bstack1ll11lll111_opy_],
    ):
        self.bstack1lllll1l111_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(bstack1ll1111111l_opy_, TestFramework.bstack1lllllllll1_opy_)
        req.execution_context.hash = str(bstack1ll1111111l_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll1111111l_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll1111111l_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll1111111l_opy_, TestFramework.bstack1llll11llll_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll1111111l_opy_, TestFramework.bstack1lll1l11l11_opy_)
            log_entry.uuid = TestFramework.get_state(bstack1ll1111111l_opy_, TestFramework.bstack1llll11ll1l_opy_)
            log_entry.test_framework_state = bstack1ll1111111l_opy_.state.name
            log_entry.message = entry.message.encode(bstack1ll1l_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤ᐀"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack1ll1l_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨᐁ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll11ll11ll_opy_
                log_entry.file_path = entry.bstack1ll1ll_opy_
        def bstack1ll1l1ll1l1_opy_():
            bstack1l11l11lll_opy_ = datetime.now()
            try:
                self.bstack1llll1l1ll1_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l11ll1111l_opy_:
                    bstack1ll1111111l_opy_.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡷࡪࡴࡤࡠ࡮ࡲ࡫ࡤࡩࡲࡦࡣࡷࡩࡩࡥࡥࡷࡧࡱࡸࡤࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤᐂ"), datetime.now() - bstack1l11l11lll_opy_)
                elif entry.kind == TestFramework.bstack1l11l1llll1_opy_:
                    bstack1ll1111111l_opy_.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࡥࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠥᐃ"), datetime.now() - bstack1l11l11lll_opy_)
                else:
                    bstack1ll1111111l_opy_.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠢࡨࡴࡳࡧ࠿ࡹࡥ࡯ࡦࡢࡰࡴ࡭࡟ࡤࡴࡨࡥࡹ࡫ࡤࡠࡧࡹࡩࡳࡺ࡟࡭ࡱࡪࠦᐄ"), datetime.now() - bstack1l11l11lll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1ll1l_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨᐅ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11lllll_opy_.enqueue(bstack1ll1l1ll1l1_opy_)
    @measure(event_name=EVENTS.bstack1l11ll111ll_opy_, stage=STAGE.bstack11lll11ll_opy_)
    def bstack1l11l1l1111_opy_(
        self,
        instance: bstack1lll1l1l1ll_opy_,
        bstack1llllll111l_opy_: Tuple[bstack1llll11l1ll_opy_, bstack1lll1llll11_opy_],
        event_json=None,
    ):
        self.bstack1lllll1l111_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1lllllllll1_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll11llll_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l11l11_opy_)
        req.test_framework_state = bstack1llllll111l_opy_[0].name
        req.test_hook_state = bstack1llllll111l_opy_[1].name
        started_at = TestFramework.get_state(instance, TestFramework.bstack1ll11l11l11_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.get_state(instance, TestFramework.bstack1ll11llllll_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l11l1111l1_opy_)).encode(bstack1ll1l_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᐆ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1ll1l1ll1l1_opy_():
            bstack1l11l11lll_opy_ = datetime.now()
            try:
                self.bstack1llll1l1ll1_opy_.TestFrameworkEvent(req)
                instance.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡦࡸࡨࡲࡹࠨᐇ"), datetime.now() - bstack1l11l11lll_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1ll1l_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤᐈ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11lllll_opy_.enqueue(bstack1ll1l1ll1l1_opy_)
    def bstack1l11l1ll1l1_opy_(self, instance: bstack1llllllll1l_opy_):
        bstack1l11l1l11ll_opy_ = TestFramework.bstack1l11l11l11l_opy_(instance.context)
        for t in bstack1l11l1l11ll_opy_:
            bstack1lll11l11l1_opy_ = TestFramework.get_state(t, bstack1lll11l1ll1_opy_.bstack1llll1l11l1_opy_, [])
            if any(instance is d[1] for d in bstack1lll11l11l1_opy_):
                return t
    def bstack1l11ll11lll_opy_(self, message):
        self.bstack1l11l11ll1l_opy_(message + bstack1ll1l_opy_ (u"ࠧࡢ࡮ࠣᐉ"))
    def log_error(self, message):
        self.bstack1l11l11l111_opy_(message + bstack1ll1l_opy_ (u"ࠨ࡜࡯ࠤᐊ"))
    def bstack1l11ll111l1_opy_(self, level, original_func):
        def bstack1l11l1ll111_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            if bstack1ll1l_opy_ (u"ࠢࡆࡸࡨࡲࡹࡊࡩࡴࡲࡤࡸࡨ࡮ࡥࡳࡏࡲࡨࡺࡲࡥࠣᐋ") in message or bstack1ll1l_opy_ (u"ࠣ࡝ࡖࡈࡐࡉࡌࡊ࡟ࠥᐌ") in message or bstack1ll1l_opy_ (u"ࠤ࡞࡛ࡪࡨࡄࡳ࡫ࡹࡩࡷࡓ࡯ࡥࡷ࡯ࡩࡢࠨᐍ") in message:
                return return_value
            bstack1l11l1l11ll_opy_ = TestFramework.bstack1l11l1lll1l_opy_()
            if not bstack1l11l1l11ll_opy_:
                return return_value
            bstack1ll1111111l_opy_ = next(
                (
                    instance
                    for instance in bstack1l11l1l11ll_opy_
                    if TestFramework.bstack1lllll11lll_opy_(instance, TestFramework.bstack1llll11ll1l_opy_)
                ),
                None,
            )
            if not bstack1ll1111111l_opy_:
                return return_value
            entry = bstack1ll11lll111_opy_(TestFramework.bstack1ll11l1l11l_opy_, message, level)
            self.bstack1ll1l1ll111_opy_(bstack1ll1111111l_opy_, [entry])
            return return_value
        return bstack1l11l1ll111_opy_
    def bstack1l11ll11l11_opy_(self):
        def bstack1l11l1l1l11_opy_(*args, **kwargs):
            try:
                self.bstack1l11ll1l1ll_opy_(*args, **kwargs)
                if not args:
                    return
                message = bstack1ll1l_opy_ (u"ࠪࠤࠬᐎ").join(str(arg) for arg in args)
                if not message.strip():
                    return
                if bstack1ll1l_opy_ (u"ࠦࡊࡼࡥ࡯ࡶࡇ࡭ࡸࡶࡡࡵࡥ࡫ࡩࡷࡓ࡯ࡥࡷ࡯ࡩࠧᐏ") in message:
                    return
                bstack1l11l1l11ll_opy_ = TestFramework.bstack1l11l1lll1l_opy_()
                if not bstack1l11l1l11ll_opy_:
                    return
                bstack1ll1111111l_opy_ = next(
                    (
                        instance
                        for instance in bstack1l11l1l11ll_opy_
                        if TestFramework.bstack1lllll11lll_opy_(instance, TestFramework.bstack1llll11ll1l_opy_)
                    ),
                    None,
                )
                if not bstack1ll1111111l_opy_:
                    return
                entry = bstack1ll11lll111_opy_(TestFramework.bstack1ll11l1l11l_opy_, message, bstack1l1l11l1lll_opy_.bstack1l11l1l1l1l_opy_)
                self.bstack1ll1l1ll111_opy_(bstack1ll1111111l_opy_, [entry])
            except Exception as e:
                try:
                    self.bstack1l11ll1l1ll_opy_(bstack1lllll1l1_opy_ (u"ࠧࡡࡅࡷࡧࡱࡸࡉ࡯ࡳࡱࡣࡷࡧ࡭࡫ࡲࡎࡱࡧࡹࡱ࡫࡝ࠡࡎࡲ࡫ࠥࡩࡡࡱࡶࡸࡶࡪࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡦࡿࠥᐐ"))
                except:
                    pass
        return bstack1l11l1l1l11_opy_
    def bstack1l11l1l11l1_opy_(self, event: dict, instance=None) -> None:
        global _1ll11l11111_opy_
        levels = [bstack1ll1l_opy_ (u"ࠨࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠤᐑ"), bstack1ll1l_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦᐒ")]
        bstack1l11l1lll11_opy_ = bstack1ll1l_opy_ (u"ࠣࠤᐓ")
        if instance is not None:
            try:
                bstack1l11l1lll11_opy_ = TestFramework.get_state(instance, TestFramework.bstack1llll11ll1l_opy_)
            except Exception as e:
                self.logger.warning(bstack1ll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡸࡹ࡮ࡪࠠࡧࡴࡲࡱࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠢᐔ").format(e))
        bstack1l11l1ll11l_opy_ = []
        try:
            for level in levels:
                platform_index = os.environ[bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪᐕ")]
                bstack1ll1ll111l1_opy_ = os.path.join(bstack1ll1111llll_opy_, (bstack1ll1l11lll1_opy_ + str(platform_index)), level)
                if not os.path.isdir(bstack1ll1ll111l1_opy_):
                    self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠠ࡯ࡱࡷࠤࡵࡸࡥࡴࡧࡱࡸࠥ࡬࡯ࡳࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡔࡦࡵࡷࠤࡦࡴࡤࠡࡄࡸ࡭ࡱࡪࠠ࡭ࡧࡹࡩࡱࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࢀࢃࠢᐖ").format(bstack1ll1ll111l1_opy_))
                    continue
                file_names = os.listdir(bstack1ll1ll111l1_opy_)
                for file_name in file_names:
                    file_path = os.path.join(bstack1ll1ll111l1_opy_, file_name)
                    abs_path = os.path.abspath(file_path)
                    if abs_path in _1ll11l11111_opy_:
                        self.logger.info(bstack1ll1l_opy_ (u"ࠧࡖࡡࡵࡪࠣࡥࡱࡸࡥࡢࡦࡼࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡼࡿࠥᐗ").format(abs_path))
                        continue
                    if os.path.isfile(file_path):
                        try:
                            bstack1l11l1l1ll1_opy_ = os.path.getmtime(file_path)
                            timestamp = datetime.fromtimestamp(bstack1l11l1l1ll1_opy_, tz=timezone.utc).isoformat()
                            file_size = os.path.getsize(file_path)
                            if level == bstack1ll1l_opy_ (u"ࠨࡔࡦࡵࡷࡐࡪࡼࡥ࡭ࠤᐘ"):
                                entry = bstack1ll11lll111_opy_(
                                    kind=bstack1ll1l_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤᐙ"),
                                    message=bstack1ll1l_opy_ (u"ࠣࠤᐚ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll11ll11ll_opy_=file_size,
                                    bstack1l1llllllll_opy_=bstack1ll1l_opy_ (u"ࠤࡐࡅࡓ࡛ࡁࡍࡡࡘࡔࡑࡕࡁࡅࠤᐛ"),
                                    bstack1ll1ll_opy_=os.path.abspath(file_path),
                                    bstack1lllll111l_opy_=bstack1l11l1lll11_opy_
                                )
                            elif level == bstack1ll1l_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢᐜ"):
                                entry = bstack1ll11lll111_opy_(
                                    kind=bstack1ll1l_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨᐝ"),
                                    message=bstack1ll1l_opy_ (u"ࠧࠨᐞ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll11ll11ll_opy_=file_size,
                                    bstack1l1llllllll_opy_=bstack1ll1l_opy_ (u"ࠨࡍࡂࡐࡘࡅࡑࡥࡕࡑࡎࡒࡅࡉࠨᐟ"),
                                    bstack1ll1ll_opy_=os.path.abspath(file_path),
                                    bstack1ll11llll1l_opy_=bstack1l11l1lll11_opy_
                                )
                            bstack1l11l1ll11l_opy_.append(entry)
                            _1ll11l11111_opy_.add(abs_path)
                        except Exception as bstack1l11l1111ll_opy_:
                            self.logger.error(bstack1ll1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡶࡦ࡯ࡳࡦࡦࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡿࢂࠨᐠ").format(bstack1l11l1111ll_opy_))
        except Exception as e:
            self.logger.error(bstack1ll1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡷࡧࡩࡴࡧࡧࠤࡼ࡮ࡥ࡯ࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡶࠤࢀࢃࠢᐡ").format(e))
        event[bstack1ll1l_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢᐢ")] = bstack1l11l1ll11l_opy_
class bstack1l11l1111l1_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l11l111l11_opy_ = set()
        kwargs[bstack1ll1l_opy_ (u"ࠥࡷࡰ࡯ࡰ࡬ࡧࡼࡷࠧᐣ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l11ll11111_opy_(obj, self.bstack1l11l111l11_opy_)
def bstack1l11l1ll1ll_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l11ll11111_opy_(obj, bstack1l11l111l11_opy_=None, max_depth=3):
    if bstack1l11l111l11_opy_ is None:
        bstack1l11l111l11_opy_ = set()
    if id(obj) in bstack1l11l111l11_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l11l111l11_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1l11l111l1l_opy_ = TestFramework.bstack1ll11l1ll11_opy_(obj)
    bstack1l11l1l1lll_opy_ = next((k.lower() in bstack1l11l111l1l_opy_.lower() for k in bstack1l11l111ll1_opy_.keys()), None)
    if bstack1l11l1l1lll_opy_:
        obj = TestFramework.bstack1ll111lll1l_opy_(obj, bstack1l11l111ll1_opy_[bstack1l11l1l1lll_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack1ll1l_opy_ (u"ࠦࡤࡥࡳ࡭ࡱࡷࡷࡤࡥࠢᐤ")):
            keys = getattr(obj, bstack1ll1l_opy_ (u"ࠧࡥ࡟ࡴ࡮ࡲࡸࡸࡥ࡟ࠣᐥ"), [])
        elif hasattr(obj, bstack1ll1l_opy_ (u"ࠨ࡟ࡠࡦ࡬ࡧࡹࡥ࡟ࠣᐦ")):
            keys = getattr(obj, bstack1ll1l_opy_ (u"ࠢࡠࡡࡧ࡭ࡨࡺ࡟ࡠࠤᐧ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack1ll1l_opy_ (u"ࠣࡡࠥᐨ"))}
        if not obj and bstack1l11l111l1l_opy_ == bstack1ll1l_opy_ (u"ࠤࡳࡥࡹ࡮࡬ࡪࡤ࠱ࡔࡴࡹࡩࡹࡒࡤࡸ࡭ࠨᐩ"):
            obj = {bstack1ll1l_opy_ (u"ࠥࡴࡦࡺࡨࠣᐪ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l11l1ll1ll_opy_(key) or str(key).startswith(bstack1ll1l_opy_ (u"ࠦࡤࠨᐫ")):
            continue
        if value is not None and bstack1l11l1ll1ll_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l11ll11111_opy_(value, bstack1l11l111l11_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l11ll11111_opy_(o, bstack1l11l111l11_opy_, max_depth) for o in value]))
    return result or None