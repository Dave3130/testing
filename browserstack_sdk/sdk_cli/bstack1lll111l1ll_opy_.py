# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1llll1ll1l1_opy_ import (
    bstack1llll1lll1l_opy_,
    bstack1lllll1l1ll_opy_,
    bstack1lll111l1l1_opy_,
    bstack1lllllll1l1_opy_,
    bstack1lll1l111l1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lllll11l1l_opy_ import bstack1lllll11111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll11l1lll_opy_, bstack1llll111111_opy_, bstack1lll1lll1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11ll1l1_opy_ import bstack1lll11lll11_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1l1111l_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll111lll1_opy_(bstack1lll11lll11_opy_):
    bstack1lll11ll11l_opy_ = bstack111l1l_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡥࡴ࡬ࡺࡪࡸࡳࠣᅻ")
    bstack1lll11ll1ll_opy_ = bstack111l1l_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤᅼ")
    bstack1lll1l1ll11_opy_ = bstack111l1l_opy_ (u"ࠦࡳࡵ࡮ࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨᅽ")
    bstack1lll1ll1111_opy_ = bstack111l1l_opy_ (u"ࠧࡺࡥࡴࡶࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᅾ")
    bstack1lll1l1lll1_opy_ = bstack111l1l_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡤࡸࡥࡧࡵࠥᅿ")
    bstack1lll1ll1l11_opy_ = bstack111l1l_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡩࡲࡦࡣࡷࡩࡩࠨᆀ")
    bstack1llll111l11_opy_ = bstack111l1l_opy_ (u"ࠣࡥࡥࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡥ࡮ࡢ࡯ࡨࠦᆁ")
    bstack1lll1lll1l1_opy_ = bstack111l1l_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡴࡶࡤࡸࡺࡹࠢᆂ")
    def __init__(self):
        super().__init__(bstack1llll11111l_opy_=self.bstack1lll11ll11l_opy_, frameworks=[bstack1lllll11111_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllllll111_opy_((bstack1lll11l1lll_opy_.BEFORE_EACH, bstack1llll111111_opy_.POST), self.bstack1lll111111l_opy_)
        TestFramework.bstack1lllllll111_opy_((bstack1lll11l1lll_opy_.TEST, bstack1llll111111_opy_.PRE), self.bstack1lll1l11111_opy_)
        TestFramework.bstack1lllllll111_opy_((bstack1lll11l1lll_opy_.TEST, bstack1llll111111_opy_.POST), self.bstack1lll1l11ll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll111111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1ll_opy_,
        bstack1llll1l11l1_opy_: Tuple[bstack1lll11l1lll_opy_, bstack1llll111111_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll1111ll1_opy_ = self.bstack1lll111ll1l_opy_(instance.context)
        if not bstack1lll1111ll1_opy_:
            self.logger.debug(bstack111l1l_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡥࡴ࡬ࡺࡪࡸࡳ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨᆃ") + str(bstack1llll1l11l1_opy_) + bstack111l1l_opy_ (u"ࠦࠧᆄ"))
        f.bstack1llll1l111l_opy_(instance, bstack1lll111lll1_opy_.bstack1lll11ll1ll_opy_, bstack1lll1111ll1_opy_)
        bstack1lll11111l1_opy_ = self.bstack1lll111ll1l_opy_(instance.context, bstack1lll11l111l_opy_=False)
        f.bstack1llll1l111l_opy_(instance, bstack1lll111lll1_opy_.bstack1lll1l1ll11_opy_, bstack1lll11111l1_opy_)
    def bstack1lll1l11111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1ll_opy_,
        bstack1llll1l11l1_opy_: Tuple[bstack1lll11l1lll_opy_, bstack1llll111111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111111l_opy_(f, instance, bstack1llll1l11l1_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll111l11_opy_, False):
            self.__1lll1111111_opy_(f,instance,bstack1llll1l11l1_opy_)
    def bstack1lll1l11ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1ll_opy_,
        bstack1llll1l11l1_opy_: Tuple[bstack1lll11l1lll_opy_, bstack1llll111111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111111l_opy_(f, instance, bstack1llll1l11l1_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll111lll1_opy_.bstack1llll111l11_opy_, False):
            self.__1lll1111111_opy_(f, instance, bstack1llll1l11l1_opy_)
        if not f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1lll1l1_opy_, False):
            self.__1ll1lllllll_opy_(f, instance, bstack1llll1l11l1_opy_)
    def bstack1lll111llll_opy_(
        self,
        f: bstack1lllll11111_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll1l1_opy_, str],
        bstack1llll1l11l1_opy_: Tuple[bstack1llll1lll1l_opy_, bstack1lllll1l1ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll11l1111_opy_(instance):
            return
        if f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1lll1l1_opy_, False):
            return
        driver.execute_script(
            bstack111l1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠥᆅ").format(
                json.dumps(
                    {
                        bstack111l1l_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨᆆ"): bstack111l1l_opy_ (u"ࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠥᆇ"),
                        bstack111l1l_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦᆈ"): {bstack111l1l_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤᆉ"): result},
                    }
                )
            )
        )
        f.bstack1llll1l111l_opy_(instance, bstack1lll111lll1_opy_.bstack1lll1lll1l1_opy_, True)
    def bstack1lll111ll1l_opy_(self, context: bstack1lll1l111l1_opy_, bstack1lll11l111l_opy_= True):
        if bstack1lll11l111l_opy_:
            bstack1lll1111ll1_opy_ = self.bstack1llll111l1l_opy_(context, reverse=True)
        else:
            bstack1lll1111ll1_opy_ = self.bstack1llll1111ll_opy_(context, reverse=True)
        return [f for f in bstack1lll1111ll1_opy_ if f[1].state != bstack1llll1lll1l_opy_.QUIT]
    @measure(event_name=EVENTS.bstack11lll1ll1_opy_, stage=STAGE.bstack1ll1ll111_opy_)
    def __1ll1lllllll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1ll_opy_,
        bstack1llll1l11l1_opy_: Tuple[bstack1lll11l1lll_opy_, bstack1llll111111_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack111l1l_opy_ (u"ࠥࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠣᆊ")).get(bstack111l1l_opy_ (u"ࠦࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣᆋ")):
            bstack1lll1111ll1_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll11ll1ll_opy_, [])
            if not bstack1lll1111ll1_opy_:
                self.logger.debug(bstack111l1l_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡧࡶ࡮ࡼࡥࡳࡵ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᆌ") + str(bstack1llll1l11l1_opy_) + bstack111l1l_opy_ (u"ࠨࠢᆍ"))
                return
            driver = bstack1lll1111ll1_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1lll1ll1l1l_opy_, None)
            if not status:
                self.logger.debug(bstack111l1l_opy_ (u"ࠢࡴࡧࡷࡣࡦࡩࡴࡪࡸࡨࡣࡩࡸࡩࡷࡧࡵࡷ࠿ࠦ࡮ࡰࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡴࡦࡵࡷ࠰ࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤᆎ") + str(bstack1llll1l11l1_opy_) + bstack111l1l_opy_ (u"ࠣࠤᆏ"))
                return
            bstack1lll1l1l1ll_opy_ = {bstack111l1l_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤᆐ"): status.lower()}
            bstack1lll11llll1_opy_ = f.get_state(instance, TestFramework.bstack1lll1ll11ll_opy_, None)
            if status.lower() == bstack111l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᆑ") and bstack1lll11llll1_opy_ is not None:
                bstack1lll1l1l1ll_opy_[bstack111l1l_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᆒ")] = bstack1lll11llll1_opy_[0][bstack111l1l_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᆓ")][0] if isinstance(bstack1lll11llll1_opy_, list) else str(bstack1lll11llll1_opy_)
            driver.execute_script(
                bstack111l1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠦᆔ").format(
                    json.dumps(
                        {
                            bstack111l1l_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢᆕ"): bstack111l1l_opy_ (u"ࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦᆖ"),
                            bstack111l1l_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᆗ"): bstack1lll1l1l1ll_opy_,
                        }
                    )
                )
            )
            f.bstack1llll1l111l_opy_(instance, bstack1lll111lll1_opy_.bstack1lll1lll1l1_opy_, True)
    @measure(event_name=EVENTS.bstack1lll11l11l_opy_, stage=STAGE.bstack1ll1ll111_opy_)
    def __1lll1111111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1ll_opy_,
        bstack1llll1l11l1_opy_: Tuple[bstack1lll11l1lll_opy_, bstack1llll111111_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack111l1l_opy_ (u"ࠥࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠣᆘ")).get(bstack111l1l_opy_ (u"ࠦࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨᆙ")):
            test_name = f.get_state(instance, TestFramework.bstack1lll1111l11_opy_, None)
            if not test_name:
                self.logger.debug(bstack111l1l_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡶࡨࡷࡹࠦ࡮ࡢ࡯ࡨࠦᆚ"))
                return
            bstack1lll1111ll1_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll11ll1ll_opy_, [])
            if not bstack1lll1111ll1_opy_:
                self.logger.debug(bstack111l1l_opy_ (u"ࠨࡳࡦࡶࡢࡥࡨࡺࡩࡷࡧࡢࡨࡷ࡯ࡶࡦࡴࡶ࠾ࠥࡴ࡯ࠡࡵࡷࡥࡹࡻࡳࠡࡨࡲࡶࠥࡺࡥࡴࡶ࠯ࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࠣᆛ") + str(bstack1llll1l11l1_opy_) + bstack111l1l_opy_ (u"ࠢࠣᆜ"))
                return
            for bstack1lll1111l1l_opy_, bstack1lll111l111_opy_ in bstack1lll1111ll1_opy_:
                if not bstack1lllll11111_opy_.bstack1lll11l1111_opy_(bstack1lll111l111_opy_):
                    continue
                driver = bstack1lll1111l1l_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack111l1l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂࠨᆝ").format(
                        json.dumps(
                            {
                                bstack111l1l_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࠤᆞ"): bstack111l1l_opy_ (u"ࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦᆟ"),
                                bstack111l1l_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᆠ"): {bstack111l1l_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᆡ"): test_name},
                            }
                        )
                    )
                )
            f.bstack1llll1l111l_opy_(instance, bstack1lll111lll1_opy_.bstack1llll111l11_opy_, True)
    def bstack1lll1l1ll1l_opy_(
        self,
        instance: bstack1lll1lll1ll_opy_,
        f: TestFramework,
        bstack1llll1l11l1_opy_: Tuple[bstack1lll11l1lll_opy_, bstack1llll111111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111111l_opy_(f, instance, bstack1llll1l11l1_opy_, *args, **kwargs)
        bstack1lll1111ll1_opy_ = [d for d, _ in f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll11ll1ll_opy_, [])]
        if not bstack1lll1111ll1_opy_:
            self.logger.debug(bstack111l1l_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡷࡪࡹࡳࡪࡱࡱࡷࠥࡺ࡯ࠡ࡮࡬ࡲࡰࠨᆢ"))
            return
        if not bstack1lll1l1111l_opy_():
            self.logger.debug(bstack111l1l_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧᆣ"))
            return
        for bstack1lll1111lll_opy_ in bstack1lll1111ll1_opy_:
            driver = bstack1lll1111lll_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack111l1l_opy_ (u"ࠣࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡔࡻࡱࡧ࠿ࠨᆤ") + str(timestamp)
            driver.execute_script(
                bstack111l1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠢᆥ").format(
                    json.dumps(
                        {
                            bstack111l1l_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࠥᆦ"): bstack111l1l_opy_ (u"ࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨᆧ"),
                            bstack111l1l_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣᆨ"): {
                                bstack111l1l_opy_ (u"ࠨࡴࡺࡲࡨࠦᆩ"): bstack111l1l_opy_ (u"ࠢࡂࡰࡱࡳࡹࡧࡴࡪࡱࡱࠦᆪ"),
                                bstack111l1l_opy_ (u"ࠣࡦࡤࡸࡦࠨᆫ"): data,
                                bstack111l1l_opy_ (u"ࠤ࡯ࡩࡻ࡫࡬ࠣᆬ"): bstack111l1l_opy_ (u"ࠥࡨࡪࡨࡵࡨࠤᆭ")
                            }
                        }
                    )
                )
            )
    def bstack1lll1lll111_opy_(
        self,
        instance: bstack1lll1lll1ll_opy_,
        f: TestFramework,
        bstack1llll1l11l1_opy_: Tuple[bstack1lll11l1lll_opy_, bstack1llll111111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111111l_opy_(f, instance, bstack1llll1l11l1_opy_, *args, **kwargs)
        keys = [
            bstack1lll111lll1_opy_.bstack1lll11ll1ll_opy_,
            bstack1lll111lll1_opy_.bstack1lll1l1ll11_opy_,
        ]
        bstack1lll1111ll1_opy_ = []
        for key in keys:
            bstack1lll1111ll1_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll1111ll1_opy_:
            self.logger.debug(bstack111l1l_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡻ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡡ࡯ࡻࠣࡷࡪࡹࡳࡪࡱࡱࡷࠥࡺ࡯ࠡ࡮࡬ࡲࡰࠨᆮ"))
            return
        if f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1ll1l11_opy_, False):
            self.logger.debug(bstack111l1l_opy_ (u"ࠧࡵ࡮ࡠࡣࡩࡸࡪࡸ࡟ࡵࡧࡶࡸ࠿ࠦࡃࡃࡖࠣࡥࡱࡸࡥࡢࡦࡼࠤࡨࡸࡥࡢࡶࡨࡨࠧᆯ"))
            return
        self.bstack1llllll11l1_opy_()
        bstack1l1ll111ll_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llll11llll_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll1111l1_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll11l1ll1_opy_)
        req.test_framework_state = bstack1llll1l11l1_opy_[0].name
        req.test_hook_state = bstack1llll1l11l1_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll1ll1lll_opy_)
        for bstack1lll1111l1l_opy_, driver in bstack1lll1111ll1_opy_:
            try:
                webdriver = bstack1lll1111l1l_opy_()
                if webdriver is None:
                    self.logger.debug(bstack111l1l_opy_ (u"ࠨࡗࡦࡤࡇࡶ࡮ࡼࡥࡳࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠤ࡮ࡹࠠࡏࡱࡱࡩࠥ࠮ࡲࡦࡨࡨࡶࡪࡴࡣࡦࠢࡨࡼࡵ࡯ࡲࡦࡦࠬࠦᆰ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack111l1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠨᆱ")
                    if bstack1lllll11111_opy_.get_state(driver, bstack1lllll11111_opy_.bstack1lll111l11l_opy_, False)
                    else bstack111l1l_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࡡࡪࡶ࡮ࡪࠢᆲ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1lllll11111_opy_.get_state(driver, bstack1lllll11111_opy_.bstack1lll1l11lll_opy_, bstack111l1l_opy_ (u"ࠤࠥᆳ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1lllll11111_opy_.get_state(driver, bstack1lllll11111_opy_.bstack1lll1l11l1l_opy_, bstack111l1l_opy_ (u"ࠥࠦᆴ"))
                caps = None
                if hasattr(webdriver, bstack111l1l_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᆵ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack111l1l_opy_ (u"࡙ࠧࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭࡮ࡼࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࡪࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡤࡪࡴࡨࡧࡹࡲࡹࠡࡨࡵࡳࡲࠦࡤࡳ࡫ࡹࡩࡷ࠴ࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᆶ"))
                    except Exception as e:
                        self.logger.debug(bstack111l1l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡪࡩࡹࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠥ࡬ࡲࡰ࡯ࠣࡨࡷ࡯ࡶࡦࡴ࠱ࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ࠼ࠣࠦᆷ") + str(e) + bstack111l1l_opy_ (u"ࠢࠣᆸ"))
                try:
                    bstack1lll11111ll_opy_ = json.dumps(caps).encode(bstack111l1l_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢᆹ")) if caps else bstack1lll111ll11_opy_ (u"ࠤࡾࢁࠧᆺ")
                    req.capabilities = bstack1lll11111ll_opy_
                except Exception as e:
                    self.logger.debug(bstack111l1l_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡤࡤࡷࡣࡪࡼࡥ࡯ࡶ࠽ࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡱࡨࠥࡹࡥࡳ࡫ࡤࡰ࡮ࢀࡥࠡࡥࡤࡴࡸࠦࡦࡰࡴࠣࡶࡪࡷࡵࡦࡵࡷ࠾ࠥࠨᆻ") + str(e) + bstack111l1l_opy_ (u"ࠦࠧᆼ"))
            except Exception as e:
                self.logger.error(bstack111l1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡦࡵ࡭ࡻ࡫ࡲࠡ࡫ࡷࡩࡲࡀࠠࠣᆽ") + str(str(e)) + bstack111l1l_opy_ (u"ࠨࠢᆾ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1llllll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1ll_opy_,
        bstack1llll1l11l1_opy_: Tuple[bstack1lll11l1lll_opy_, bstack1llll111111_opy_],
        *args,
        **kwargs
    ):
        bstack1lll1111ll1_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll11ll1ll_opy_, [])
        if not bstack1lll1l1111l_opy_() and len(bstack1lll1111ll1_opy_) == 0:
            bstack1lll1111ll1_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1l1ll11_opy_, [])
        if not bstack1lll1111ll1_opy_:
            self.logger.debug(bstack111l1l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᆿ") + str(kwargs) + bstack111l1l_opy_ (u"ࠣࠤᇀ"))
            return {}
        if len(bstack1lll1111ll1_opy_) > 1:
            self.logger.debug(bstack111l1l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࢀࡲࡥ࡯ࠪࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᇁ") + str(kwargs) + bstack111l1l_opy_ (u"ࠥࠦᇂ"))
            return {}
        bstack1lll1111l1l_opy_, bstack1lll1lllll1_opy_ = bstack1lll1111ll1_opy_[0]
        driver = bstack1lll1111l1l_opy_()
        if not driver:
            self.logger.debug(bstack111l1l_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᇃ") + str(kwargs) + bstack111l1l_opy_ (u"ࠧࠨᇄ"))
            return {}
        capabilities = f.get_state(bstack1lll1lllll1_opy_, bstack1lllll11111_opy_.bstack1lll1l1l11l_opy_)
        if not capabilities:
            self.logger.debug(bstack111l1l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠣࡪࡴࡻ࡮ࡥࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᇅ") + str(kwargs) + bstack111l1l_opy_ (u"ࠢࠣᇆ"))
            return {}
        return capabilities.get(bstack111l1l_opy_ (u"ࠣࡣ࡯ࡻࡦࡿࡳࡎࡣࡷࡧ࡭ࠨᇇ"), {})
    def bstack1lll1l1l1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1lll1ll_opy_,
        bstack1llll1l11l1_opy_: Tuple[bstack1lll11l1lll_opy_, bstack1llll111111_opy_],
        *args,
        **kwargs
    ):
        bstack1lll1111ll1_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll11ll1ll_opy_, [])
        if not bstack1lll1l1111l_opy_() and len(bstack1lll1111ll1_opy_) == 0:
            bstack1lll1111ll1_opy_ = f.get_state(instance, bstack1lll111lll1_opy_.bstack1lll1l1ll11_opy_, [])
        if not bstack1lll1111ll1_opy_:
            self.logger.debug(bstack111l1l_opy_ (u"ࠤࡪࡩࡹࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡨࡷ࡯ࡶࡦࡴ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᇈ") + str(kwargs) + bstack111l1l_opy_ (u"ࠥࠦᇉ"))
            return
        if len(bstack1lll1111ll1_opy_) > 1:
            self.logger.debug(bstack111l1l_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡪࡲࡪࡸࡨࡶ࠿ࠦࡻ࡭ࡧࡱࠬࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡳࡵࡣࡱࡧࡪࡹࠩࡾࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᇊ") + str(kwargs) + bstack111l1l_opy_ (u"ࠧࠨᇋ"))
        bstack1lll1111l1l_opy_, bstack1lll1lllll1_opy_ = bstack1lll1111ll1_opy_[0]
        driver = bstack1lll1111l1l_opy_()
        if not driver:
            self.logger.debug(bstack111l1l_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᇌ") + str(kwargs) + bstack111l1l_opy_ (u"ࠢࠣᇍ"))
            return
        return driver