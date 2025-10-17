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
from datetime import datetime, timezone
import os
import builtins
from pathlib import Path
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1111111lll_opy_ import bstack1llll1l1l11_opy_, bstack1llllll1111_opy_, bstack1llll1l11ll_opy_
from browserstack_sdk.sdk_cli.bstack1llllll11ll_opy_ import bstack1lllll1l1l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll111ll1l_opy_ import bstack1lll111llll_opy_
from browserstack_sdk.sdk_cli.bstack1llllll1l11_opy_ import bstack1llll1l11l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll111l_opy_, bstack1lll1l11l11_opy_, bstack1lll1l1ll11_opy_, bstack1ll1l11ll1l_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1lll1ll1lll_opy_, bstack1ll11ll111l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1l11l1l11ll_opy_ = [bstack11111_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᎟"), bstack11111_opy_ (u"ࠧࡶࡡࡳࡧࡱࡸࠧᎠ"), bstack11111_opy_ (u"ࠨࡣࡰࡰࡩ࡭࡬ࠨᎡ"), bstack11111_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࠣᎢ"), bstack11111_opy_ (u"ࠣࡲࡤࡸ࡭ࠨᎣ")]
bstack1ll11l1l1l1_opy_ = bstack1ll11ll111l_opy_()
bstack1ll1l1ll1ll_opy_ = bstack11111_opy_ (u"ࠤࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠮ࠤᎤ")
bstack1l11l1l1111_opy_ = {
    bstack11111_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡴࡾࡺࡨࡰࡰ࠱ࡍࡹ࡫࡭ࠣᎥ"): bstack1l11l1l11ll_opy_,
    bstack11111_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡵࡿࡴࡩࡱࡱ࠲ࡕࡧࡣ࡬ࡣࡪࡩࠧᎦ"): bstack1l11l1l11ll_opy_,
    bstack11111_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡶࡹࡵࡪࡲࡲ࠳ࡓ࡯ࡥࡷ࡯ࡩࠧᎧ"): bstack1l11l1l11ll_opy_,
    bstack11111_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡰࡺࡶ࡫ࡳࡳ࠴ࡃ࡭ࡣࡶࡷࠧᎨ"): bstack1l11l1l11ll_opy_,
    bstack11111_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡱࡻࡷ࡬ࡴࡴ࠮ࡇࡷࡱࡧࡹ࡯࡯࡯ࠤᎩ"): bstack1l11l1l11ll_opy_
    + [
        bstack11111_opy_ (u"ࠣࡱࡵ࡭࡬࡯࡮ࡢ࡮ࡱࡥࡲ࡫ࠢᎪ"),
        bstack11111_opy_ (u"ࠤ࡮ࡩࡾࡽ࡯ࡳࡦࡶࠦᎫ"),
        bstack11111_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨ࡭ࡳ࡬࡯ࠣᎬ"),
        bstack11111_opy_ (u"ࠦࡰ࡫ࡹࡸࡱࡵࡨࡸࠨᎭ"),
        bstack11111_opy_ (u"ࠧࡩࡡ࡭࡮ࡶࡴࡪࡩࠢᎮ"),
        bstack11111_opy_ (u"ࠨࡣࡢ࡮࡯ࡳࡧࡰࠢᎯ"),
        bstack11111_opy_ (u"ࠢࡴࡶࡤࡶࡹࠨᎰ"),
        bstack11111_opy_ (u"ࠣࡵࡷࡳࡵࠨᎱ"),
        bstack11111_opy_ (u"ࠤࡧࡹࡷࡧࡴࡪࡱࡱࠦᎲ"),
        bstack11111_opy_ (u"ࠥࡻ࡭࡫࡮ࠣᎳ"),
    ],
    bstack11111_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡲࡧࡩ࡯࠰ࡖࡩࡸࡹࡩࡰࡰࠥᎴ"): [bstack11111_opy_ (u"ࠧࡹࡴࡢࡴࡷࡴࡦࡺࡨࠣᎵ"), bstack11111_opy_ (u"ࠨࡴࡦࡵࡷࡷ࡫ࡧࡩ࡭ࡧࡧࠦᎶ"), bstack11111_opy_ (u"ࠢࡵࡧࡶࡸࡸࡩ࡯࡭࡮ࡨࡧࡹ࡫ࡤࠣᎷ"), bstack11111_opy_ (u"ࠣ࡫ࡷࡩࡲࡹࠢᎸ")],
    bstack11111_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡦࡳࡳ࡬ࡩࡨ࠰ࡆࡳࡳ࡬ࡩࡨࠤᎹ"): [bstack11111_opy_ (u"ࠥ࡭ࡳࡼ࡯ࡤࡣࡷ࡭ࡴࡴ࡟ࡱࡣࡵࡥࡲࡹࠢᎺ"), bstack11111_opy_ (u"ࠦࡦࡸࡧࡴࠤᎻ")],
    bstack11111_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳࡬ࡩࡹࡶࡸࡶࡪࡹ࠮ࡇ࡫ࡻࡸࡺࡸࡥࡅࡧࡩࠦᎼ"): [bstack11111_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧᎽ"), bstack11111_opy_ (u"ࠢࡢࡴࡪࡲࡦࡳࡥࠣᎾ"), bstack11111_opy_ (u"ࠣࡨࡸࡲࡨࠨᎿ"), bstack11111_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࡴࠤᏀ"), bstack11111_opy_ (u"ࠥࡹࡳ࡯ࡴࡵࡧࡶࡸࠧᏁ"), bstack11111_opy_ (u"ࠦ࡮ࡪࡳࠣᏂ")],
    bstack11111_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳࡬ࡩࡹࡶࡸࡶࡪࡹ࠮ࡔࡷࡥࡖࡪࡷࡵࡦࡵࡷࠦᏃ"): [bstack11111_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࠦᏄ"), bstack11111_opy_ (u"ࠢࡱࡣࡵࡥࡲࠨᏅ"), bstack11111_opy_ (u"ࠣࡲࡤࡶࡦࡳ࡟ࡪࡰࡧࡩࡽࠨᏆ")],
    bstack11111_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡵࡹࡳࡴࡥࡳ࠰ࡆࡥࡱࡲࡉ࡯ࡨࡲࠦᏇ"): [bstack11111_opy_ (u"ࠥࡻ࡭࡫࡮ࠣᏈ"), bstack11111_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷࠦᏉ")],
    bstack11111_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡳࡡࡳ࡭࠱ࡷࡹࡸࡵࡤࡶࡸࡶࡪࡹ࠮ࡏࡱࡧࡩࡐ࡫ࡹࡸࡱࡵࡨࡸࠨᏊ"): [bstack11111_opy_ (u"ࠨ࡮ࡰࡦࡨࠦᏋ"), bstack11111_opy_ (u"ࠢࡱࡣࡵࡩࡳࡺࠢᏌ")],
    bstack11111_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯࡯ࡤࡶࡰ࠴ࡳࡵࡴࡸࡧࡹࡻࡲࡦࡵ࠱ࡑࡦࡸ࡫ࠣᏍ"): [bstack11111_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᏎ"), bstack11111_opy_ (u"ࠥࡥࡷ࡭ࡳࠣᏏ"), bstack11111_opy_ (u"ࠦࡰࡽࡡࡳࡩࡶࠦᏐ")],
}
_1ll1111lll1_opy_ = set()
class bstack1l1l111l1l1_opy_(bstack1lllll1l1l1_opy_):
    bstack1l11l111111_opy_ = bstack11111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡨࡪ࡬ࡥࡳࡴࡨࡨࠧᏑ")
    bstack1l11l1l1lll_opy_ = bstack11111_opy_ (u"ࠨࡉࡏࡈࡒࠦᏒ")
    bstack1l11l1ll1ll_opy_ = bstack11111_opy_ (u"ࠢࡆࡔࡕࡓࡗࠨᏓ")
    bstack1l11l1l1l1l_opy_: Callable
    bstack1l11l1l111l_opy_: Callable
    def __init__(self, bstack1l1l1l11l1l_opy_, bstack1ll1lll1l11_opy_):
        super().__init__()
        self.bstack1l11ll1l11l_opy_ = bstack1ll1lll1l11_opy_
        if os.getenv(bstack11111_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡐ࠳࠴࡝ࠧᏔ"), bstack11111_opy_ (u"ࠤ࠴ࠦᏕ")) != bstack11111_opy_ (u"ࠥ࠵ࠧᏖ") or not self.is_enabled():
            self.logger.warning(bstack11111_opy_ (u"ࠦࠧᏗ") + str(self.__class__.__name__) + bstack11111_opy_ (u"ࠧࠦࡤࡪࡵࡤࡦࡱ࡫ࡤࠣᏘ"))
            return
        TestFramework.bstack1lllll11111_opy_((bstack1lll1ll111l_opy_.TEST, bstack1lll1l1ll11_opy_.PRE), self.bstack1llll11l1ll_opy_)
        TestFramework.bstack1lllll11111_opy_((bstack1lll1ll111l_opy_.TEST, bstack1lll1l1ll11_opy_.POST), self.bstack1lll1l1l1ll_opy_)
        for event in bstack1lll1ll111l_opy_:
            for state in bstack1lll1l1ll11_opy_:
                TestFramework.bstack1lllll11111_opy_((event, state), self.bstack1l11l111l11_opy_)
        bstack1l1l1l11l1l_opy_.bstack1lllll11111_opy_((bstack1llllll1111_opy_.bstack1llllll1lll_opy_, bstack1llll1l11ll_opy_.POST), self.bstack1l11ll11lll_opy_)
        self.bstack1l11l1l1l1l_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l11ll11ll1_opy_(bstack1l1l111l1l1_opy_.bstack1l11l1l1lll_opy_, self.bstack1l11l1l1l1l_opy_)
        self.bstack1l11l1l111l_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l11ll11ll1_opy_(bstack1l1l111l1l1_opy_.bstack1l11l1ll1ll_opy_, self.bstack1l11l1l111l_opy_)
        self.bstack1l11l1llll1_opy_ = builtins.print
        builtins.print = self.bstack1l11l11ll11_opy_()
    def is_enabled(self) -> bool:
        return True
    def bstack1l11l111l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1ll11111l11_opy_() and instance:
            bstack1l111lllll1_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1lllllll1ll_opy_
            if test_framework_state == bstack1lll1ll111l_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1lll1ll111l_opy_.LOG:
                bstack1lll11l111_opy_ = datetime.now()
                entries = f.bstack1ll1l1lll1l_opy_(instance, bstack1lllllll1ll_opy_)
                if entries:
                    self.bstack1ll1l1ll11l_opy_(instance, entries)
                    instance.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࠨᏙ"), datetime.now() - bstack1lll11l111_opy_)
                    f.bstack1ll111l11l1_opy_(instance, bstack1lllllll1ll_opy_)
                instance.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠢࡰ࠳࠴ࡽ࠿ࡵ࡮ࡠࡣ࡯ࡰࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵࡵࠥᏚ"), datetime.now() - bstack1l111lllll1_opy_)
                return # do not send this event with the bstack1l11ll11111_opy_ bstack1l11l1111l1_opy_
            elif (
                test_framework_state == bstack1lll1ll111l_opy_.TEST
                and test_hook_state == bstack1lll1l1ll11_opy_.POST
                and not f.bstack1llllllll1l_opy_(instance, TestFramework.bstack1ll111lll1l_opy_)
            ):
                self.logger.warning(bstack11111_opy_ (u"ࠣࡦࡵࡳࡵࡶࡩ࡯ࡩࠣࡨࡺ࡫ࠠࡵࡱࠣࡰࡦࡩ࡫ࠡࡱࡩࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࠨᏛ") + str(TestFramework.bstack1llllllll1l_opy_(instance, TestFramework.bstack1ll111lll1l_opy_)) + bstack11111_opy_ (u"ࠤࠥᏜ"))
                f.bstack11111111ll_opy_(instance, bstack1l1l111l1l1_opy_.bstack1l11l111111_opy_, True)
                return # do not send this event bstack1l11l1ll11l_opy_ bstack1l11l11l1ll_opy_
            elif (
                f.get_state(instance, bstack1l1l111l1l1_opy_.bstack1l11l111111_opy_, False)
                and test_framework_state == bstack1lll1ll111l_opy_.LOG_REPORT
                and test_hook_state == bstack1lll1l1ll11_opy_.POST
                and f.bstack1llllllll1l_opy_(instance, TestFramework.bstack1ll111lll1l_opy_)
            ):
                self.logger.warning(bstack11111_opy_ (u"ࠥ࡭ࡳࡰࡥࡤࡶ࡬ࡲ࡬ࠦࡔࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡙ࡴࡢࡶࡨ࠲࡙ࡋࡓࡕ࠮ࠣࡘࡪࡹࡴࡉࡱࡲ࡯ࡘࡺࡡࡵࡧ࠱ࡔࡔ࡙ࡔࠡࠤᏝ") + str(TestFramework.bstack1llllllll1l_opy_(instance, TestFramework.bstack1ll111lll1l_opy_)) + bstack11111_opy_ (u"ࠦࠧᏞ"))
                self.bstack1l11l111l11_opy_(f, instance, (bstack1lll1ll111l_opy_.TEST, bstack1lll1l1ll11_opy_.POST), *args, **kwargs)
            bstack1lll11l111_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l11ll1111l_opy_ = sorted(
                filter(lambda x: x.get(bstack11111_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠣᏟ"), None), data.pop(bstack11111_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨᏠ"), {}).values()),
                key=lambda x: x[bstack11111_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠥᏡ")],
            )
            if bstack1lll111llll_opy_.bstack1llll111ll1_opy_ in data:
                data.pop(bstack1lll111llll_opy_.bstack1llll111ll1_opy_)
            data.update({bstack11111_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠣᏢ"): bstack1l11ll1111l_opy_})
            instance.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠤ࡭ࡷࡴࡴ࠺ࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠢᏣ"), datetime.now() - bstack1lll11l111_opy_)
            bstack1lll11l111_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l11ll11l1l_opy_)
            instance.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠥ࡮ࡸࡵ࡮࠻ࡱࡱࡣࡦࡲ࡬ࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸࡸࠨᏤ"), datetime.now() - bstack1lll11l111_opy_)
            self.bstack1l11l1111l1_opy_(instance, bstack1lllllll1ll_opy_, event_json=event_json)
            instance.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠦࡴ࠷࠱ࡺ࠼ࡲࡲࡤࡧ࡬࡭ࡡࡷࡩࡸࡺ࡟ࡦࡸࡨࡲࡹࡹࠢᏥ"), datetime.now() - bstack1l111lllll1_opy_)
    def bstack1llll11l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack11l1ll11l_opy_ import bstack111111l11l_opy_
        bstack1l1lllll1ll_opy_ = bstack111111l11l_opy_.bstack1ll1l11l1l1_opy_(EVENTS.bstack111llll1l_opy_.value)
        self.bstack1l11ll1l11l_opy_.bstack1lll1lllll1_opy_(instance, f, bstack1lllllll1ll_opy_, *args, **kwargs)
        bstack111111l11l_opy_.end(EVENTS.bstack111llll1l_opy_.value, bstack1l1lllll1ll_opy_ + bstack11111_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᏦ"), bstack1l1lllll1ll_opy_ + bstack11111_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᏧ"), status=True, failure=None, test_name=None)
    def bstack1lll1l1l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1l11ll1l11l_opy_.bstack1llll11l11l_opy_(instance, f, bstack1lllllll1ll_opy_, *args, **kwargs)
        self.bstack1l11l11ll1l_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1l11l1l11l1_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1l11l11ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack11111_opy_ (u"ࠢࡔ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡗࡩࡸࡺࡓࡦࡵࡶ࡭ࡴࡴࡅࡷࡧࡱࡸࠥ࡭ࡒࡑࡅࠣࡧࡦࡲ࡬࠻ࠢࡑࡳࠥࡼࡡ࡭࡫ࡧࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡪࡡࡵࡣࠥᏨ"))
            return
        bstack1lll11l111_opy_ = datetime.now()
        try:
            r = self.bstack1llll1lll11_opy_.TestSessionEvent(req)
            instance.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡹ࡫ࡳࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡩࡻ࡫࡮ࡵࠤᏩ"), datetime.now() - bstack1lll11l111_opy_)
            f.bstack11111111ll_opy_(instance, self.bstack1l11ll1l11l_opy_.bstack1llll111l11_opy_, r.success)
            if not r.success:
                self.logger.info(bstack11111_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦᏪ") + str(r) + bstack11111_opy_ (u"ࠥࠦᏫ"))
        except grpc.RpcError as e:
            self.logger.error(bstack11111_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤᏬ") + str(e) + bstack11111_opy_ (u"ࠧࠨᏭ"))
            traceback.print_exc()
            raise e
    def bstack1l11ll11lll_opy_(
        self,
        f: bstack1llll1l11l1_opy_,
        _driver: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        _1l11ll1l1l1_opy_: Tuple[bstack1llllll1111_opy_, bstack1llll1l11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1llll1l11l1_opy_.bstack1l1lll11lll_opy_(method_name):
            return
        if f.bstack1l1lll11l11_opy_(*args) == bstack1llll1l11l1_opy_.bstack1l11l111ll1_opy_:
            bstack1l111lllll1_opy_ = datetime.now()
            screenshot = result.get(bstack11111_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࠧᏮ"), None) if isinstance(result, dict) else None
            if not isinstance(screenshot, str) or len(screenshot) <= 0:
                self.logger.warning(bstack11111_opy_ (u"ࠢࡪࡰࡹࡥࡱ࡯ࡤࠡࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠥ࡯࡭ࡢࡩࡨࠤࡧࡧࡳࡦ࠸࠷ࠤࡸࡺࡲࠣᏯ"))
                return
            bstack1ll111lll11_opy_ = self.bstack1l11l1lll1l_opy_(instance)
            if bstack1ll111lll11_opy_:
                entry = bstack1ll1l11ll1l_opy_(TestFramework.bstack1l11l1111ll_opy_, screenshot)
                self.bstack1ll1l1ll11l_opy_(bstack1ll111lll11_opy_, [entry])
                instance.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠣࡱ࠴࠵ࡾࡀ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡧࡻࡩࡨࡻࡴࡦࠤᏰ"), datetime.now() - bstack1l111lllll1_opy_)
            else:
                self.logger.warning(bstack11111_opy_ (u"ࠤࡸࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡶࡨࡷࡹࠦࡦࡰࡴࠣࡻ࡭࡯ࡣࡩࠢࡷ࡬࡮ࡹࠠࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠤࡼࡧࡳࠡࡶࡤ࡯ࡪࡴࠠࡣࡻࠣࡨࡷ࡯ࡶࡦࡴࡀࠤࢀࢃࠢᏱ").format(instance.ref()))
        event = {}
        bstack1ll111lll11_opy_ = self.bstack1l11l1lll1l_opy_(instance)
        if bstack1ll111lll11_opy_:
            self.bstack1l11l11l11l_opy_(event, bstack1ll111lll11_opy_)
            if event.get(bstack11111_opy_ (u"ࠥࡰࡴ࡭ࡳࠣᏲ")):
                self.bstack1ll1l1ll11l_opy_(bstack1ll111lll11_opy_, event[bstack11111_opy_ (u"ࠦࡱࡵࡧࡴࠤᏳ")])
            else:
                self.logger.debug(bstack11111_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤࡱࡵࡧࡴࠢࡩࡳࡷࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣࡩࡻ࡫࡮ࡵࠤᏴ"))
    @measure(event_name=EVENTS.bstack1l11l1lllll_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1ll1l1ll11l_opy_(
        self,
        bstack1ll111lll11_opy_: bstack1lll1l11l11_opy_,
        entries: List[bstack1ll1l11ll1l_opy_],
    ):
        self.bstack1lllll1lll1_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(bstack1ll111lll11_opy_, TestFramework.bstack1lllll1111l_opy_)
        req.execution_context.hash = str(bstack1ll111lll11_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1ll111lll11_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1ll111lll11_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.get_state(bstack1ll111lll11_opy_, TestFramework.bstack1llll111l1l_opy_)
            log_entry.test_framework_version = TestFramework.get_state(bstack1ll111lll11_opy_, TestFramework.bstack1lll1l111l1_opy_)
            log_entry.uuid = TestFramework.get_state(bstack1ll111lll11_opy_, TestFramework.bstack1lll11lllll_opy_)
            log_entry.test_framework_state = bstack1ll111lll11_opy_.state.name
            log_entry.message = entry.message.encode(bstack11111_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᏵ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack11111_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤ᏶"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1ll1l1111ll_opy_
                log_entry.file_path = entry.bstack1l1l1ll_opy_
        def bstack1ll111111ll_opy_():
            bstack1lll11l111_opy_ = datetime.now()
            try:
                self.bstack1llll1lll11_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l11l1111ll_opy_:
                    bstack1ll111lll11_opy_.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠧ᏷"), datetime.now() - bstack1lll11l111_opy_)
                elif entry.kind == TestFramework.bstack1l11l1l1l11_opy_:
                    bstack1ll111lll11_opy_.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠨᏸ"), datetime.now() - bstack1lll11l111_opy_)
                else:
                    bstack1ll111lll11_opy_.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡰࡴ࡭ࠢᏹ"), datetime.now() - bstack1lll11l111_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11111_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤᏺ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11lll1l_opy_.enqueue(bstack1ll111111ll_opy_)
    @measure(event_name=EVENTS.bstack1l11ll111ll_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def bstack1l11l1111l1_opy_(
        self,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        event_json=None,
    ):
        self.bstack1lllll1lll1_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1lllll1111l_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll111l1l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l111l1_opy_)
        req.test_framework_state = bstack1lllllll1ll_opy_[0].name
        req.test_hook_state = bstack1lllllll1ll_opy_[1].name
        started_at = TestFramework.get_state(instance, TestFramework.bstack1ll111ll11l_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.get_state(instance, TestFramework.bstack1ll1l1l1ll1_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l11ll11l1l_opy_)).encode(bstack11111_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦᏻ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1ll111111ll_opy_():
            bstack1lll11l111_opy_ = datetime.now()
            try:
                self.bstack1llll1lll11_opy_.TestFrameworkEvent(req)
                instance.bstack1l1l111l1_opy_(bstack11111_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡩࡻ࡫࡮ࡵࠤᏼ"), datetime.now() - bstack1lll11l111_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack11111_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᏽ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack1lll11lll1l_opy_.enqueue(bstack1ll111111ll_opy_)
    def bstack1l11l1lll1l_opy_(self, instance: bstack1llll1l1l11_opy_):
        bstack1l11l111lll_opy_ = TestFramework.bstack1l11l1ll1l1_opy_(instance.context)
        for t in bstack1l11l111lll_opy_:
            bstack1lll11ll1ll_opy_ = TestFramework.get_state(t, bstack1lll111llll_opy_.bstack1llll111ll1_opy_, [])
            if any(instance is d[1] for d in bstack1lll11ll1ll_opy_):
                return t
    def bstack1l11l1lll11_opy_(self, message):
        self.bstack1l11l1l1l1l_opy_(message + bstack11111_opy_ (u"ࠣ࡞ࡱࠦ᏾"))
    def log_error(self, message):
        self.bstack1l11l1l111l_opy_(message + bstack11111_opy_ (u"ࠤ࡟ࡲࠧ᏿"))
    def bstack1l11ll11ll1_opy_(self, level, original_func):
        def bstack1l11ll11l11_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            if bstack11111_opy_ (u"ࠥࡉࡻ࡫࡮ࡵࡆ࡬ࡷࡵࡧࡴࡤࡪࡨࡶࡒࡵࡤࡶ࡮ࡨࠦ᐀") in message or bstack11111_opy_ (u"ࠦࡠ࡙ࡄࡌࡅࡏࡍࡢࠨᐁ") in message or bstack11111_opy_ (u"ࠧࡡࡗࡦࡤࡇࡶ࡮ࡼࡥࡳࡏࡲࡨࡺࡲࡥ࡞ࠤᐂ") in message:
                return return_value
            bstack1l11l111lll_opy_ = TestFramework.bstack1l11l11llll_opy_()
            if not bstack1l11l111lll_opy_:
                return return_value
            bstack1ll111lll11_opy_ = next(
                (
                    instance
                    for instance in bstack1l11l111lll_opy_
                    if TestFramework.bstack1llllllll1l_opy_(instance, TestFramework.bstack1lll11lllll_opy_)
                ),
                None,
            )
            if not bstack1ll111lll11_opy_:
                return return_value
            entry = bstack1ll1l11ll1l_opy_(TestFramework.bstack1ll11l1ll11_opy_, message, level)
            self.bstack1ll1l1ll11l_opy_(bstack1ll111lll11_opy_, [entry])
            return return_value
        return bstack1l11ll11l11_opy_
    def bstack1l11l11ll11_opy_(self):
        def bstack1l11ll111l1_opy_(*args, **kwargs):
            try:
                self.bstack1l11l1llll1_opy_(*args, **kwargs)
                if not args:
                    return
                message = bstack11111_opy_ (u"࠭ࠠࠨᐃ").join(str(arg) for arg in args)
                if not message.strip():
                    return
                if bstack11111_opy_ (u"ࠢࡆࡸࡨࡲࡹࡊࡩࡴࡲࡤࡸࡨ࡮ࡥࡳࡏࡲࡨࡺࡲࡥࠣᐄ") in message:
                    return
                bstack1l11l111lll_opy_ = TestFramework.bstack1l11l11llll_opy_()
                if not bstack1l11l111lll_opy_:
                    return
                bstack1ll111lll11_opy_ = next(
                    (
                        instance
                        for instance in bstack1l11l111lll_opy_
                        if TestFramework.bstack1llllllll1l_opy_(instance, TestFramework.bstack1lll11lllll_opy_)
                    ),
                    None,
                )
                if not bstack1ll111lll11_opy_:
                    return
                entry = bstack1ll1l11ll1l_opy_(TestFramework.bstack1ll11l1ll11_opy_, message, bstack1l1l111l1l1_opy_.bstack1l11l1l1lll_opy_)
                self.bstack1ll1l1ll11l_opy_(bstack1ll111lll11_opy_, [entry])
            except Exception as e:
                try:
                    self.bstack1l11l1llll1_opy_(bstack1lll1ll11ll_opy_ (u"ࠣ࡝ࡈࡺࡪࡴࡴࡅ࡫ࡶࡴࡦࡺࡣࡩࡧࡵࡑࡴࡪࡵ࡭ࡧࡠࠤࡑࡵࡧࠡࡥࡤࡴࡹࡻࡲࡦࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࡩࢂࠨᐅ"))
                except:
                    pass
        return bstack1l11ll111l1_opy_
    def bstack1l11l11l11l_opy_(self, event: dict, instance=None) -> None:
        global _1ll1111lll1_opy_
        levels = [bstack11111_opy_ (u"ࠤࡗࡩࡸࡺࡌࡦࡸࡨࡰࠧᐆ"), bstack11111_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࠢᐇ")]
        bstack1l11l11lll1_opy_ = bstack11111_opy_ (u"ࠦࠧᐈ")
        if instance is not None:
            try:
                bstack1l11l11lll1_opy_ = TestFramework.get_state(instance, TestFramework.bstack1lll11lllll_opy_)
            except Exception as e:
                self.logger.warning(bstack11111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡻࡵࡪࡦࠣࡪࡷࡵ࡭ࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠥᐉ").format(e))
        bstack1l11ll1l111_opy_ = []
        try:
            for level in levels:
                platform_index = os.environ[bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᐊ")]
                bstack1ll111ll111_opy_ = os.path.join(bstack1ll11l1l1l1_opy_, (bstack1ll1l1ll1ll_opy_ + str(platform_index)), level)
                if not os.path.isdir(bstack1ll111ll111_opy_):
                    self.logger.debug(bstack11111_opy_ (u"ࠢࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡲࡴࡺࠠࡱࡴࡨࡷࡪࡴࡴࠡࡨࡲࡶࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡗࡩࡸࡺࠠࡢࡰࡧࠤࡇࡻࡩ࡭ࡦࠣࡰࡪࡼࡥ࡭ࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡼࡿࠥᐋ").format(bstack1ll111ll111_opy_))
                    continue
                file_names = os.listdir(bstack1ll111ll111_opy_)
                for file_name in file_names:
                    file_path = os.path.join(bstack1ll111ll111_opy_, file_name)
                    abs_path = os.path.abspath(file_path)
                    if abs_path in _1ll1111lll1_opy_:
                        self.logger.info(bstack11111_opy_ (u"ࠣࡒࡤࡸ࡭ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡿࢂࠨᐌ").format(abs_path))
                        continue
                    if os.path.isfile(file_path):
                        try:
                            bstack1l11l11111l_opy_ = os.path.getmtime(file_path)
                            timestamp = datetime.fromtimestamp(bstack1l11l11111l_opy_, tz=timezone.utc).isoformat()
                            file_size = os.path.getsize(file_path)
                            if level == bstack11111_opy_ (u"ࠤࡗࡩࡸࡺࡌࡦࡸࡨࡰࠧᐍ"):
                                entry = bstack1ll1l11ll1l_opy_(
                                    kind=bstack11111_opy_ (u"ࠥࡘࡊ࡙ࡔࡠࡃࡗࡘࡆࡉࡈࡎࡇࡑࡘࠧᐎ"),
                                    message=bstack11111_opy_ (u"ࠦࠧᐏ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll1l1111ll_opy_=file_size,
                                    bstack1ll11ll11ll_opy_=bstack11111_opy_ (u"ࠧࡓࡁࡏࡗࡄࡐࡤ࡛ࡐࡍࡑࡄࡈࠧᐐ"),
                                    bstack1l1l1ll_opy_=os.path.abspath(file_path),
                                    bstack11l1lll1ll_opy_=bstack1l11l11lll1_opy_
                                )
                            elif level == bstack11111_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠥᐑ"):
                                entry = bstack1ll1l11ll1l_opy_(
                                    kind=bstack11111_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤᐒ"),
                                    message=bstack11111_opy_ (u"ࠣࠤᐓ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1ll1l1111ll_opy_=file_size,
                                    bstack1ll11ll11ll_opy_=bstack11111_opy_ (u"ࠤࡐࡅࡓ࡛ࡁࡍࡡࡘࡔࡑࡕࡁࡅࠤᐔ"),
                                    bstack1l1l1ll_opy_=os.path.abspath(file_path),
                                    bstack1ll11l11lll_opy_=bstack1l11l11lll1_opy_
                                )
                            bstack1l11ll1l111_opy_.append(entry)
                            _1ll1111lll1_opy_.add(abs_path)
                        except Exception as bstack1l111llllll_opy_:
                            self.logger.error(bstack11111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡲࡢ࡫ࡶࡩࡩࠦࡷࡩࡧࡱࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸࠦࡻࡾࠤᐕ").format(bstack1l111llllll_opy_))
        except Exception as e:
            self.logger.error(bstack11111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡳࡣ࡬ࡷࡪࡪࠠࡸࡪࡨࡲࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡼࡿࠥᐖ").format(e))
        event[bstack11111_opy_ (u"ࠧࡲ࡯ࡨࡵࠥᐗ")] = bstack1l11ll1l111_opy_
class bstack1l11ll11l1l_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l11l111l1l_opy_ = set()
        kwargs[bstack11111_opy_ (u"ࠨࡳ࡬࡫ࡳ࡯ࡪࡿࡳࠣᐘ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l11l11l111_opy_(obj, self.bstack1l11l111l1l_opy_)
def bstack1l11l11l1l1_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l11l11l111_opy_(obj, bstack1l11l111l1l_opy_=None, max_depth=3):
    if bstack1l11l111l1l_opy_ is None:
        bstack1l11l111l1l_opy_ = set()
    if id(obj) in bstack1l11l111l1l_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l11l111l1l_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1l11l1l1ll1_opy_ = TestFramework.bstack1ll1111llll_opy_(obj)
    bstack1l11l1ll111_opy_ = next((k.lower() in bstack1l11l1l1ll1_opy_.lower() for k in bstack1l11l1l1111_opy_.keys()), None)
    if bstack1l11l1ll111_opy_:
        obj = TestFramework.bstack1ll111l1lll_opy_(obj, bstack1l11l1l1111_opy_[bstack1l11l1ll111_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack11111_opy_ (u"ࠢࡠࡡࡶࡰࡴࡺࡳࡠࡡࠥᐙ")):
            keys = getattr(obj, bstack11111_opy_ (u"ࠣࡡࡢࡷࡱࡵࡴࡴࡡࡢࠦᐚ"), [])
        elif hasattr(obj, bstack11111_opy_ (u"ࠤࡢࡣࡩ࡯ࡣࡵࡡࡢࠦᐛ")):
            keys = getattr(obj, bstack11111_opy_ (u"ࠥࡣࡤࡪࡩࡤࡶࡢࡣࠧᐜ"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack11111_opy_ (u"ࠦࡤࠨᐝ"))}
        if not obj and bstack1l11l1l1ll1_opy_ == bstack11111_opy_ (u"ࠧࡶࡡࡵࡪ࡯࡭ࡧ࠴ࡐࡰࡵ࡬ࡼࡕࡧࡴࡩࠤᐞ"):
            obj = {bstack11111_opy_ (u"ࠨࡰࡢࡶ࡫ࠦᐟ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l11l11l1l1_opy_(key) or str(key).startswith(bstack11111_opy_ (u"ࠢࡠࠤᐠ")):
            continue
        if value is not None and bstack1l11l11l1l1_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l11l11l111_opy_(value, bstack1l11l111l1l_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l11l11l111_opy_(o, bstack1l11l111l1l_opy_, max_depth) for o in value]))
    return result or None