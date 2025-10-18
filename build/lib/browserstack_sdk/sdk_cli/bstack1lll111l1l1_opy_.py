# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1llllll1l1l_opy_ import (
    bstack1llll1ll1l1_opy_,
    bstack1lllll1ll1l_opy_,
    bstack1lll1111ll1_opy_,
    bstack1lllll11l1l_opy_,
    bstack1lll1l111l1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll1ll1_opy_ import bstack1lllll1l1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_, bstack1llll1111l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lll11l_opy_ import bstack1lll11lllll_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1l1ll1l_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll11l1111_opy_(bstack1lll11lllll_opy_):
    bstack1lll1lll111_opy_ = bstack11ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡥࡴ࡬ࡺࡪࡸࡳࠣᆂ")
    bstack1lll1l1llll_opy_ = bstack11ll_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤᆃ")
    bstack1lll1l11l11_opy_ = bstack11ll_opy_ (u"ࠦࡳࡵ࡮ࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨᆄ")
    bstack1lll1l111ll_opy_ = bstack11ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᆅ")
    bstack1lll11ll1ll_opy_ = bstack11ll_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡤࡸࡥࡧࡵࠥᆆ")
    bstack1lll1l1l11l_opy_ = bstack11ll_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡩࡲࡦࡣࡷࡩࡩࠨᆇ")
    bstack1lll1l1l111_opy_ = bstack11ll_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥ࡮ࡢ࡯ࡨࠦᆈ")
    bstack1lll11l1ll1_opy_ = bstack11ll_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡴࡶࡤࡸࡺࡹࠢᆉ")
    def __init__(self):
        super().__init__(bstack1lll11ll111_opy_=self.bstack1lll1lll111_opy_, frameworks=[bstack1lllll1l1l1_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllll1l1ll_opy_((bstack1lll1l1ll11_opy_.BEFORE_EACH, bstack1lll1ll111l_opy_.POST), self.bstack1lll111l1ll_opy_)
        TestFramework.bstack1lllll1l1ll_opy_((bstack1lll1l1ll11_opy_.TEST, bstack1lll1ll111l_opy_.PRE), self.bstack1lll1lll1l1_opy_)
        TestFramework.bstack1lllll1l1ll_opy_((bstack1lll1l1ll11_opy_.TEST, bstack1lll1ll111l_opy_.POST), self.bstack1lll1l11lll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll111l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll1111l1l_opy_ = self.bstack1lll1111111_opy_(instance.context)
        if not bstack1lll1111l1l_opy_:
            self.logger.debug(bstack11ll_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡥࡴ࡬ࡺࡪࡸࡳ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨᆊ") + str(bstack1lllll1l11l_opy_) + bstack11ll_opy_ (u"ࠦࠧᆋ"))
        f.bstack1llllll1lll_opy_(instance, bstack1lll11l1111_opy_.bstack1lll1l1llll_opy_, bstack1lll1111l1l_opy_)
        bstack1lll111llll_opy_ = self.bstack1lll1111111_opy_(instance.context, bstack1lll111111l_opy_=False)
        f.bstack1llllll1lll_opy_(instance, bstack1lll11l1111_opy_.bstack1lll1l11l11_opy_, bstack1lll111llll_opy_)
    def bstack1lll1lll1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111l1ll_opy_(f, instance, bstack1lllll1l11l_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll1l1l111_opy_, False):
            self.__1lll111ll11_opy_(f,instance,bstack1lllll1l11l_opy_)
    def bstack1lll1l11lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111l1ll_opy_(f, instance, bstack1lllll1l11l_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll1l1l111_opy_, False):
            self.__1lll111ll11_opy_(f, instance, bstack1lllll1l11l_opy_)
        if not f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll11l1ll1_opy_, False):
            self.__1lll11111l1_opy_(f, instance, bstack1lllll1l11l_opy_)
    def bstack1lll111l11l_opy_(
        self,
        f: bstack1lllll1l1l1_opy_,
        driver: object,
        exec: Tuple[bstack1lllll11l1l_opy_, str],
        bstack1lllll1l11l_opy_: Tuple[bstack1llll1ll1l1_opy_, bstack1lllll1ll1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll111ll1l_opy_(instance):
            return
        if f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll11l1ll1_opy_, False):
            return
        driver.execute_script(
            bstack11ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠥᆌ").format(
                json.dumps(
                    {
                        bstack11ll_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨᆍ"): bstack11ll_opy_ (u"ࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥᆎ"),
                        bstack11ll_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦᆏ"): {bstack11ll_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤᆐ"): result},
                    }
                )
            )
        )
        f.bstack1llllll1lll_opy_(instance, bstack1lll11l1111_opy_.bstack1lll11l1ll1_opy_, True)
    def bstack1lll1111111_opy_(self, context: bstack1lll1l111l1_opy_, bstack1lll111111l_opy_= True):
        if bstack1lll111111l_opy_:
            bstack1lll1111l1l_opy_ = self.bstack1lll1llllll_opy_(context, reverse=True)
        else:
            bstack1lll1111l1l_opy_ = self.bstack1lll11lll11_opy_(context, reverse=True)
        return [f for f in bstack1lll1111l1l_opy_ if f[1].state != bstack1llll1ll1l1_opy_.QUIT]
    @measure(event_name=EVENTS.bstack11ll1ll11l_opy_, stage=STAGE.bstack1ll1111l1_opy_)
    def __1lll11111l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11ll_opy_ (u"ࠥࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠣᆑ")).get(bstack11ll_opy_ (u"ࠦࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣᆒ")):
            bstack1lll1111l1l_opy_ = f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll1l1llll_opy_, [])
            if not bstack1lll1111l1l_opy_:
                self.logger.debug(bstack11ll_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡧࡶ࡮ࡼࡥࡳࡵ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᆓ") + str(bstack1lllll1l11l_opy_) + bstack11ll_opy_ (u"ࠨࠢᆔ"))
                return
            driver = bstack1lll1111l1l_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1lll11ll11l_opy_, None)
            if not status:
                self.logger.debug(bstack11ll_opy_ (u"ࠢࡴࡧࡷࡣࡦࡩࡴࡪࡸࡨࡣࡩࡸࡩࡷࡧࡵࡷ࠿ࠦ࡮ࡰࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡴࡦࡵࡷ࠰ࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤᆕ") + str(bstack1lllll1l11l_opy_) + bstack11ll_opy_ (u"ࠣࠤᆖ"))
                return
            bstack1llll111l1l_opy_ = {bstack11ll_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤᆗ"): status.lower()}
            bstack1lll1ll1111_opy_ = f.get_state(instance, TestFramework.bstack1lll1l1111l_opy_, None)
            if status.lower() == bstack11ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᆘ") and bstack1lll1ll1111_opy_ is not None:
                bstack1llll111l1l_opy_[bstack11ll_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᆙ")] = bstack1lll1ll1111_opy_[0][bstack11ll_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᆚ")][0] if isinstance(bstack1lll1ll1111_opy_, list) else str(bstack1lll1ll1111_opy_)
            driver.execute_script(
                bstack11ll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠦᆛ").format(
                    json.dumps(
                        {
                            bstack11ll_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢᆜ"): bstack11ll_opy_ (u"ࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦᆝ"),
                            bstack11ll_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᆞ"): bstack1llll111l1l_opy_,
                        }
                    )
                )
            )
            f.bstack1llllll1lll_opy_(instance, bstack1lll11l1111_opy_.bstack1lll11l1ll1_opy_, True)
    @measure(event_name=EVENTS.bstack111l1l11l1_opy_, stage=STAGE.bstack1ll1111l1_opy_)
    def __1lll111ll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11ll_opy_ (u"ࠥࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠣᆟ")).get(bstack11ll_opy_ (u"ࠦࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨᆠ")):
            test_name = f.get_state(instance, TestFramework.bstack1lll11l111l_opy_, None)
            if not test_name:
                self.logger.debug(bstack11ll_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡶࡨࡷࡹࠦ࡮ࡢ࡯ࡨࠦᆡ"))
                return
            bstack1lll1111l1l_opy_ = f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll1l1llll_opy_, [])
            if not bstack1lll1111l1l_opy_:
                self.logger.debug(bstack11ll_opy_ (u"ࠨࡳࡦࡶࡢࡥࡨࡺࡩࡷࡧࡢࡨࡷ࡯ࡶࡦࡴࡶ࠾ࠥࡴ࡯ࠡࡵࡷࡥࡹࡻࡳࠡࡨࡲࡶࠥࡺࡥࡴࡶ࠯ࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᆢ") + str(bstack1lllll1l11l_opy_) + bstack11ll_opy_ (u"ࠢࠣᆣ"))
                return
            for bstack1lll11l11l1_opy_, bstack1lll111l111_opy_ in bstack1lll1111l1l_opy_:
                if not bstack1lllll1l1l1_opy_.bstack1lll111ll1l_opy_(bstack1lll111l111_opy_):
                    continue
                driver = bstack1lll11l11l1_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack11ll_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂࠨᆤ").format(
                        json.dumps(
                            {
                                bstack11ll_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࠤᆥ"): bstack11ll_opy_ (u"ࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦᆦ"),
                                bstack11ll_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᆧ"): {bstack11ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᆨ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1llllll1lll_opy_(instance, bstack1lll11l1111_opy_.bstack1lll1l1l111_opy_, True)
    def bstack1lll1llll11_opy_(
        self,
        instance: bstack1llll1111l1_opy_,
        f: TestFramework,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111l1ll_opy_(f, instance, bstack1lllll1l11l_opy_, *args, **kwargs)
        bstack1lll1111l1l_opy_ = [d for d, _ in f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll1l1llll_opy_, [])]
        if not bstack1lll1111l1l_opy_:
            self.logger.debug(bstack11ll_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡷࡪࡹࡳࡪࡱࡱࡷࠥࡺ࡯ࠡ࡮࡬ࡲࡰࠨᆩ"))
            return
        if not bstack1lll1l1ll1l_opy_():
            self.logger.debug(bstack11ll_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᆪ"))
            return
        for bstack1lll1111lll_opy_ in bstack1lll1111l1l_opy_:
            driver = bstack1lll1111lll_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack11ll_opy_ (u"ࠣࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡔࡻࡱࡧ࠿ࠨᆫ") + str(timestamp)
            driver.execute_script(
                bstack11ll_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠢᆬ").format(
                    json.dumps(
                        {
                            bstack11ll_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࠥᆭ"): bstack11ll_opy_ (u"ࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨᆮ"),
                            bstack11ll_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣᆯ"): {
                                bstack11ll_opy_ (u"ࠨࡴࡺࡲࡨࠦᆰ"): bstack11ll_opy_ (u"ࠢࡂࡰࡱࡳࡹࡧࡴࡪࡱࡱࠦᆱ"),
                                bstack11ll_opy_ (u"ࠣࡦࡤࡸࡦࠨᆲ"): data,
                                bstack11ll_opy_ (u"ࠤ࡯ࡩࡻ࡫࡬ࠣᆳ"): bstack11ll_opy_ (u"ࠥࡨࡪࡨࡵࡨࠤᆴ")
                            }
                        }
                    )
                )
            )
    def bstack1lll1llll1l_opy_(
        self,
        instance: bstack1llll1111l1_opy_,
        f: TestFramework,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111l1ll_opy_(f, instance, bstack1lllll1l11l_opy_, *args, **kwargs)
        keys = [
            bstack1lll11l1111_opy_.bstack1lll1l1llll_opy_,
            bstack1lll11l1111_opy_.bstack1lll1l11l11_opy_,
        ]
        bstack1lll1111l1l_opy_ = []
        for key in keys:
            bstack1lll1111l1l_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll1111l1l_opy_:
            self.logger.debug(bstack11ll_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡻ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡡ࡯ࡻࠣࡷࡪࡹࡳࡪࡱࡱࡷࠥࡺ࡯ࠡ࡮࡬ࡲࡰࠨᆵ"))
            return
        if f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll1l1l11l_opy_, False):
            self.logger.debug(bstack11ll_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦࡃࡃࡖࠣࡥࡱࡸࡥࡢࡦࡼࠤࡨࡸࡥࡢࡶࡨࡨࠧᆶ"))
            return
        self.bstack1lllll111ll_opy_()
        bstack1l11111lll_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll1l111l_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1lllll1_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l11111_opy_)
        req.test_framework_state = bstack1lllll1l11l_opy_[0].name
        req.test_hook_state = bstack1lllll1l11l_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1llll111l11_opy_)
        for bstack1lll11l11l1_opy_, driver in bstack1lll1111l1l_opy_:
            try:
                webdriver = bstack1lll11l11l1_opy_()
                if webdriver is None:
                    self.logger.debug(bstack11ll_opy_ (u"ࠨࡗࡦࡤࡇࡶ࡮ࡼࡥࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤ࡮ࡹࠠࡏࡱࡱࡩࠥ࠮ࡲࡦࡨࡨࡶࡪࡴࡣࡦࠢࡨࡼࡵ࡯ࡲࡦࡦࠬࠦᆷ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack11ll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠨᆸ")
                    if bstack1lllll1l1l1_opy_.get_state(driver, bstack1lllll1l1l1_opy_.bstack1lll111lll1_opy_, False)
                    else bstack11ll_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࡡࡪࡶ࡮ࡪࠢᆹ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1lllll1l1l1_opy_.get_state(driver, bstack1lllll1l1l1_opy_.bstack1lll11lll1l_opy_, bstack11ll_opy_ (u"ࠤࠥᆺ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1lllll1l1l1_opy_.get_state(driver, bstack1lllll1l1l1_opy_.bstack1lll11llll1_opy_, bstack11ll_opy_ (u"ࠥࠦᆻ"))
                caps = None
                if hasattr(webdriver, bstack11ll_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᆼ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack11ll_opy_ (u"࡙ࠧࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭࡮ࡼࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࡪࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡤࡪࡴࡨࡧࡹࡲࡹࠡࡨࡵࡳࡲࠦࡤࡳ࡫ࡹࡩࡷ࠴ࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᆽ"))
                    except Exception as e:
                        self.logger.debug(bstack11ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡪࡩࡹࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠥ࡬ࡲࡰ࡯ࠣࡨࡷ࡯ࡶࡦࡴ࠱ࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ࠼ࠣࠦᆾ") + str(e) + bstack11ll_opy_ (u"ࠢࠣᆿ"))
                try:
                    bstack1lll1111l11_opy_ = json.dumps(caps).encode(bstack11ll_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᇀ")) if caps else bstack1lll11111ll_opy_ (u"ࠤࡾࢁࠧᇁ")
                    req.capabilities = bstack1lll1111l11_opy_
                except Exception as e:
                    self.logger.debug(bstack11ll_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡤࡤࡷࡣࡪࡼࡥ࡯ࡶ࠽ࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡱࡨࠥࡹࡥࡳ࡫ࡤࡰ࡮ࢀࡥࠡࡥࡤࡴࡸࠦࡦࡰࡴࠣࡶࡪࡷࡵࡦࡵࡷ࠾ࠥࠨᇂ") + str(e) + bstack11ll_opy_ (u"ࠦࠧᇃ"))
            except Exception as e:
                self.logger.error(bstack11ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡦࡵ࡭ࡻ࡫ࡲࠡ࡫ࡷࡩࡲࡀࠠࠣᇄ") + str(str(e)) + bstack11ll_opy_ (u"ࠨࠢᇅ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1ll1ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll1111l1l_opy_ = f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll1l1llll_opy_, [])
        if not bstack1lll1l1ll1l_opy_() and len(bstack1lll1111l1l_opy_) == 0:
            bstack1lll1111l1l_opy_ = f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll1l11l11_opy_, [])
        if not bstack1lll1111l1l_opy_:
            self.logger.debug(bstack11ll_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᇆ") + str(kwargs) + bstack11ll_opy_ (u"ࠣࠤᇇ"))
            return {}
        if len(bstack1lll1111l1l_opy_) > 1:
            self.logger.debug(bstack11ll_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᇈ") + str(kwargs) + bstack11ll_opy_ (u"ࠥࠦᇉ"))
            return {}
        bstack1lll11l11l1_opy_, bstack1lll1l1lll1_opy_ = bstack1lll1111l1l_opy_[0]
        driver = bstack1lll11l11l1_opy_()
        if not driver:
            self.logger.debug(bstack11ll_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᇊ") + str(kwargs) + bstack11ll_opy_ (u"ࠧࠨᇋ"))
            return {}
        capabilities = f.get_state(bstack1lll1l1lll1_opy_, bstack1lllll1l1l1_opy_.bstack1lll1lll1ll_opy_)
        if not capabilities:
            self.logger.debug(bstack11ll_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠣࡪࡴࡻ࡮ࡥࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᇌ") + str(kwargs) + bstack11ll_opy_ (u"ࠢࠣᇍ"))
            return {}
        return capabilities.get(bstack11ll_opy_ (u"ࠣࡣ࡯ࡻࡦࡿࡳࡎࡣࡷࡧ࡭ࠨᇎ"), {})
    def bstack1lll1l1l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1111l1_opy_,
        bstack1lllll1l11l_opy_: Tuple[bstack1lll1l1ll11_opy_, bstack1lll1ll111l_opy_],
        *args,
        **kwargs
    ):
        bstack1lll1111l1l_opy_ = f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll1l1llll_opy_, [])
        if not bstack1lll1l1ll1l_opy_() and len(bstack1lll1111l1l_opy_) == 0:
            bstack1lll1111l1l_opy_ = f.get_state(instance, bstack1lll11l1111_opy_.bstack1lll1l11l11_opy_, [])
        if not bstack1lll1111l1l_opy_:
            self.logger.debug(bstack11ll_opy_ (u"ࠤࡪࡩࡹࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡨࡷ࡯ࡶࡦࡴ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᇏ") + str(kwargs) + bstack11ll_opy_ (u"ࠥࠦᇐ"))
            return
        if len(bstack1lll1111l1l_opy_) > 1:
            self.logger.debug(bstack11ll_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡪࡲࡪࡸࡨࡶ࠿ࠦࡻ࡭ࡧࡱࠬࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᇑ") + str(kwargs) + bstack11ll_opy_ (u"ࠧࠨᇒ"))
        bstack1lll11l11l1_opy_, bstack1lll1l1lll1_opy_ = bstack1lll1111l1l_opy_[0]
        driver = bstack1lll11l11l1_opy_()
        if not driver:
            self.logger.debug(bstack11ll_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᇓ") + str(kwargs) + bstack11ll_opy_ (u"ࠢࠣᇔ"))
            return
        return driver