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
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack1111111lll_opy_ import (
    bstack1llllll1111_opy_,
    bstack1llll1l11ll_opy_,
    bstack1lll11l1ll1_opy_,
    bstack1llll1l1l11_opy_,
    bstack1lll1llll11_opy_,
)
from browserstack_sdk.sdk_cli.bstack1llllll1l11_opy_ import bstack1llll1l11l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_, bstack1lll1l11l11_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1l1l_opy_ import bstack1llll11lll1_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1ll1lll_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1lll111llll_opy_(bstack1llll11lll1_opy_):
    bstack1llll11ll1l_opy_ = bstack11111_opy_ (u"ࠧࡺࡥࡴࡶࡢࡨࡷ࡯ࡶࡦࡴࡶࠦᅍ")
    bstack1llll111ll1_opy_ = bstack11111_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࡷࠧᅎ")
    bstack1lll1ll11l1_opy_ = bstack11111_opy_ (u"ࠢ࡯ࡱࡱࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤᅏ")
    bstack1lll1l1lll1_opy_ = bstack11111_opy_ (u"ࠣࡶࡨࡷࡹࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣᅐ")
    bstack1lll1ll1l11_opy_ = bstack11111_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡠࡴࡨࡪࡸࠨᅑ")
    bstack1llll111l11_opy_ = bstack11111_opy_ (u"ࠥࡧࡧࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡥࡵࡩࡦࡺࡥࡥࠤᅒ")
    bstack1llll111lll_opy_ = bstack11111_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡱࡥࡲ࡫ࠢᅓ")
    bstack1llll11111l_opy_ = bstack11111_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡷࡹࡧࡴࡶࡵࠥᅔ")
    def __init__(self):
        super().__init__(bstack1lll1ll1ll1_opy_=self.bstack1llll11ll1l_opy_, frameworks=[bstack1llll1l11l1_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1lllll11111_opy_((bstack1lll1ll111l_opy_.BEFORE_EACH, bstack1lll1l1ll11_opy_.POST), self.bstack1lll111l11l_opy_)
        TestFramework.bstack1lllll11111_opy_((bstack1lll1ll111l_opy_.TEST, bstack1lll1l1ll11_opy_.PRE), self.bstack1llll11l1ll_opy_)
        TestFramework.bstack1lllll11111_opy_((bstack1lll1ll111l_opy_.TEST, bstack1lll1l1ll11_opy_.POST), self.bstack1lll1l1l1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll111l11l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll11ll1ll_opy_ = self.bstack1lll11l1l11_opy_(instance.context)
        if not bstack1lll11ll1ll_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠨࡳࡦࡶࡢࡥࡨࡺࡩࡷࡧࡢࡨࡷ࡯ࡶࡦࡴࡶ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࠤᅕ") + str(bstack1lllllll1ll_opy_) + bstack11111_opy_ (u"ࠢࠣᅖ"))
        f.bstack11111111ll_opy_(instance, bstack1lll111llll_opy_.bstack1llll111ll1_opy_, bstack1lll11ll1ll_opy_)
        bstack1lll11l1lll_opy_ = self.bstack1lll11l1l11_opy_(instance.context, bstack1lll111l1l1_opy_=False)
        f.bstack11111111ll_opy_(instance, bstack1lll111llll_opy_.bstack1lll1ll11l1_opy_, bstack1lll11l1lll_opy_)
    def bstack1llll11l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111l11l_opy_(f, instance, bstack1lllllll1ll_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll111llll_opy_.bstack1llll111lll_opy_, False):
            self.__1lll11ll1l1_opy_(f,instance,bstack1lllllll1ll_opy_)
    def bstack1lll1l1l1ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111l11l_opy_(f, instance, bstack1lllllll1ll_opy_, *args, **kwargs)
        if not f.get_state(instance, bstack1lll111llll_opy_.bstack1llll111lll_opy_, False):
            self.__1lll11ll1l1_opy_(f, instance, bstack1lllllll1ll_opy_)
        if not f.get_state(instance, bstack1lll111llll_opy_.bstack1llll11111l_opy_, False):
            self.__1lll111ll11_opy_(f, instance, bstack1lllllll1ll_opy_)
    def bstack1lll11l1l1l_opy_(
        self,
        f: bstack1llll1l11l1_opy_,
        driver: object,
        exec: Tuple[bstack1llll1l1l11_opy_, str],
        bstack1lllllll1ll_opy_: Tuple[bstack1llllll1111_opy_, bstack1llll1l11ll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1lll11l1111_opy_(instance):
            return
        if f.get_state(instance, bstack1lll111llll_opy_.bstack1llll11111l_opy_, False):
            return
        driver.execute_script(
            bstack11111_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂࠨᅗ").format(
                json.dumps(
                    {
                        bstack11111_opy_ (u"ࠤࡤࡧࡹ࡯࡯࡯ࠤᅘ"): bstack11111_opy_ (u"ࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨᅙ"),
                        bstack11111_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢᅚ"): {bstack11111_opy_ (u"ࠧࡹࡴࡢࡶࡸࡷࠧᅛ"): result},
                    }
                )
            )
        )
        f.bstack11111111ll_opy_(instance, bstack1lll111llll_opy_.bstack1llll11111l_opy_, True)
    def bstack1lll11l1l11_opy_(self, context: bstack1lll1llll11_opy_, bstack1lll111l1l1_opy_= True):
        if bstack1lll111l1l1_opy_:
            bstack1lll11ll1ll_opy_ = self.bstack1llll11l111_opy_(context, reverse=True)
        else:
            bstack1lll11ll1ll_opy_ = self.bstack1llll1l111l_opy_(context, reverse=True)
        return [f for f in bstack1lll11ll1ll_opy_ if f[1].state != bstack1llllll1111_opy_.QUIT]
    @measure(event_name=EVENTS.bstack11l1l111ll_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def __1lll111ll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11111_opy_ (u"ࠨࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠦᅜ")).get(bstack11111_opy_ (u"ࠢࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦᅝ")):
            bstack1lll11ll1ll_opy_ = f.get_state(instance, bstack1lll111llll_opy_.bstack1llll111ll1_opy_, [])
            if not bstack1lll11ll1ll_opy_:
                self.logger.debug(bstack11111_opy_ (u"ࠣࡵࡨࡸࡤࡧࡣࡵ࡫ࡹࡩࡤࡪࡲࡪࡸࡨࡶࡸࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࠦᅞ") + str(bstack1lllllll1ll_opy_) + bstack11111_opy_ (u"ࠤࠥᅟ"))
                return
            driver = bstack1lll11ll1ll_opy_[0][0]()
            status = f.get_state(instance, TestFramework.bstack1llll11l1l1_opy_, None)
            if not status:
                self.logger.debug(bstack11111_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡥࡴ࡬ࡺࡪࡸࡳ࠻ࠢࡱࡳࠥࡹࡴࡢࡶࡸࡷࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࠬࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧᅠ") + str(bstack1lllllll1ll_opy_) + bstack11111_opy_ (u"ࠦࠧᅡ"))
                return
            bstack1llll1111l1_opy_ = {bstack11111_opy_ (u"ࠧࡹࡴࡢࡶࡸࡷࠧᅢ"): status.lower()}
            bstack1lll1lll1ll_opy_ = f.get_state(instance, TestFramework.bstack1llll111111_opy_, None)
            if status.lower() == bstack11111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᅣ") and bstack1lll1lll1ll_opy_ is not None:
                bstack1llll1111l1_opy_[bstack11111_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧᅤ")] = bstack1lll1lll1ll_opy_[0][bstack11111_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᅥ")][0] if isinstance(bstack1lll1lll1ll_opy_, list) else str(bstack1lll1lll1ll_opy_)
            driver.execute_script(
                bstack11111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠢᅦ").format(
                    json.dumps(
                        {
                            bstack11111_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࠥᅧ"): bstack11111_opy_ (u"ࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢᅨ"),
                            bstack11111_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣᅩ"): bstack1llll1111l1_opy_,
                        }
                    )
                )
            )
            f.bstack11111111ll_opy_(instance, bstack1lll111llll_opy_.bstack1llll11111l_opy_, True)
    @measure(event_name=EVENTS.bstack11l1l1lll_opy_, stage=STAGE.bstack1111llll1l_opy_)
    def __1lll11ll1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack11111_opy_ (u"ࠨࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠦᅪ")).get(bstack11111_opy_ (u"ࠢࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤᅫ")):
            test_name = f.get_state(instance, TestFramework.bstack1lll11ll11l_opy_, None)
            if not test_name:
                self.logger.debug(bstack11111_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡱࡥࡲ࡫ࠢᅬ"))
                return
            bstack1lll11ll1ll_opy_ = f.get_state(instance, bstack1lll111llll_opy_.bstack1llll111ll1_opy_, [])
            if not bstack1lll11ll1ll_opy_:
                self.logger.debug(bstack11111_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡤࡳ࡫ࡹࡩࡷࡹ࠺ࠡࡰࡲࠤࡸࡺࡡࡵࡷࡶࠤ࡫ࡵࡲࠡࡶࡨࡷࡹ࠲ࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࠦᅭ") + str(bstack1lllllll1ll_opy_) + bstack11111_opy_ (u"ࠥࠦᅮ"))
                return
            for bstack1lll11ll111_opy_, bstack1lll11l111l_opy_ in bstack1lll11ll1ll_opy_:
                if not bstack1llll1l11l1_opy_.bstack1lll11l1111_opy_(bstack1lll11l111l_opy_):
                    continue
                driver = bstack1lll11ll111_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack11111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠤᅯ").format(
                        json.dumps(
                            {
                                bstack11111_opy_ (u"ࠧࡧࡣࡵ࡫ࡲࡲࠧᅰ"): bstack11111_opy_ (u"ࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢᅱ"),
                                bstack11111_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥᅲ"): {bstack11111_opy_ (u"ࠣࡰࡤࡱࡪࠨᅳ"): test_name},
                            }
                        )
                    )
                )
            f.bstack11111111ll_opy_(instance, bstack1lll111llll_opy_.bstack1llll111lll_opy_, True)
    def bstack1lll1lllll1_opy_(
        self,
        instance: bstack1lll1l11l11_opy_,
        f: TestFramework,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111l11l_opy_(f, instance, bstack1lllllll1ll_opy_, *args, **kwargs)
        bstack1lll11ll1ll_opy_ = [d for d, _ in f.get_state(instance, bstack1lll111llll_opy_.bstack1llll111ll1_opy_, [])]
        if not bstack1lll11ll1ll_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡳࡦࡵࡶ࡭ࡴࡴࡳࠡࡶࡲࠤࡱ࡯࡮࡬ࠤᅴ"))
            return
        if not bstack1lll1ll1lll_opy_():
            self.logger.debug(bstack11111_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣᅵ"))
            return
        for bstack1lll11l11ll_opy_ in bstack1lll11ll1ll_opy_:
            driver = bstack1lll11l11ll_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack11111_opy_ (u"ࠦࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࡗࡾࡴࡣ࠻ࠤᅶ") + str(timestamp)
            driver.execute_script(
                bstack11111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠥᅷ").format(
                    json.dumps(
                        {
                            bstack11111_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨᅸ"): bstack11111_opy_ (u"ࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤᅹ"),
                            bstack11111_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦᅺ"): {
                                bstack11111_opy_ (u"ࠤࡷࡽࡵ࡫ࠢᅻ"): bstack11111_opy_ (u"ࠥࡅࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠢᅼ"),
                                bstack11111_opy_ (u"ࠦࡩࡧࡴࡢࠤᅽ"): data,
                                bstack11111_opy_ (u"ࠧࡲࡥࡷࡧ࡯ࠦᅾ"): bstack11111_opy_ (u"ࠨࡤࡦࡤࡸ࡫ࠧᅿ")
                            }
                        }
                    )
                )
            )
    def bstack1llll11l11l_opy_(
        self,
        instance: bstack1lll1l11l11_opy_,
        f: TestFramework,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll111l11l_opy_(f, instance, bstack1lllllll1ll_opy_, *args, **kwargs)
        keys = [
            bstack1lll111llll_opy_.bstack1llll111ll1_opy_,
            bstack1lll111llll_opy_.bstack1lll1ll11l1_opy_,
        ]
        bstack1lll11ll1ll_opy_ = []
        for key in keys:
            bstack1lll11ll1ll_opy_.extend(f.get_state(instance, key, []))
        if not bstack1lll11ll1ll_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡷࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡤࡲࡾࠦࡳࡦࡵࡶ࡭ࡴࡴࡳࠡࡶࡲࠤࡱ࡯࡮࡬ࠤᆀ"))
            return
        if f.get_state(instance, bstack1lll111llll_opy_.bstack1llll111l11_opy_, False):
            self.logger.debug(bstack11111_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡆࡆ࡙ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡤࡴࡨࡥࡹ࡫ࡤࠣᆁ"))
            return
        self.bstack1lllll1lll1_opy_()
        bstack1lll11l111_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1lllll1111l_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1llll111l1l_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll1l111l1_opy_)
        req.test_framework_state = bstack1lllllll1ll_opy_[0].name
        req.test_hook_state = bstack1lllllll1ll_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll11lllll_opy_)
        for bstack1lll11ll111_opy_, driver in bstack1lll11ll1ll_opy_:
            try:
                webdriver = bstack1lll11ll111_opy_()
                if webdriver is None:
                    self.logger.debug(bstack11111_opy_ (u"ࠤ࡚ࡩࡧࡊࡲࡪࡸࡨࡶࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࠠࡪࡵࠣࡒࡴࡴࡥࠡࠪࡵࡩ࡫࡫ࡲࡦࡰࡦࡩࠥ࡫ࡸࡱ࡫ࡵࡩࡩ࠯ࠢᆂ"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack11111_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠤᆃ")
                    if bstack1llll1l11l1_opy_.get_state(driver, bstack1llll1l11l1_opy_.bstack1lll111lll1_opy_, False)
                    else bstack11111_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࡤ࡭ࡲࡪࡦࠥᆄ")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1llll1l11l1_opy_.get_state(driver, bstack1llll1l11l1_opy_.bstack1llll1l1111_opy_, bstack11111_opy_ (u"ࠧࠨᆅ"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1llll1l11l1_opy_.get_state(driver, bstack1llll1l11l1_opy_.bstack1lll1l1ll1l_opy_, bstack11111_opy_ (u"ࠨࠢᆆ"))
                caps = None
                if hasattr(webdriver, bstack11111_opy_ (u"ࠢࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠨᆇ")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack11111_opy_ (u"ࠣࡕࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࡦࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠢࡧ࡭ࡷ࡫ࡣࡵ࡮ࡼࠤ࡫ࡸ࡯࡮ࠢࡧࡶ࡮ࡼࡥࡳ࠰ࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᆈ"))
                    except Exception as e:
                        self.logger.debug(bstack11111_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡭ࡥࡵࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠡࡨࡵࡳࡲࠦࡤࡳ࡫ࡹࡩࡷ࠴ࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷ࠿ࠦࠢᆉ") + str(e) + bstack11111_opy_ (u"ࠥࠦᆊ"))
                try:
                    bstack1lll111l1ll_opy_ = json.dumps(caps).encode(bstack11111_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥᆋ")) if caps else bstack1lll11l11l1_opy_ (u"ࠧࢁࡽࠣᆌ")
                    req.capabilities = bstack1lll111l1ll_opy_
                except Exception as e:
                    self.logger.debug(bstack11111_opy_ (u"ࠨࡧࡦࡶࡢࡧࡧࡺ࡟ࡦࡸࡨࡲࡹࡀࠠࡧࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡴࡤࠡࡵࡨࡶ࡮ࡧ࡬ࡪࡼࡨࠤࡨࡧࡰࡴࠢࡩࡳࡷࠦࡲࡦࡳࡸࡩࡸࡺ࠺ࠡࠤᆍ") + str(e) + bstack11111_opy_ (u"ࠢࠣᆎ"))
            except Exception as e:
                self.logger.error(bstack11111_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡩࡸࡩࡷࡧࡵࠤ࡮ࡺࡥ࡮࠼ࠣࠦᆏ") + str(str(e)) + bstack11111_opy_ (u"ࠤࠥᆐ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1l1llll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11ll1ll_opy_ = f.get_state(instance, bstack1lll111llll_opy_.bstack1llll111ll1_opy_, [])
        if not bstack1lll1ll1lll_opy_() and len(bstack1lll11ll1ll_opy_) == 0:
            bstack1lll11ll1ll_opy_ = f.get_state(instance, bstack1lll111llll_opy_.bstack1lll1ll11l1_opy_, [])
        if not bstack1lll11ll1ll_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᆑ") + str(kwargs) + bstack11111_opy_ (u"ࠦࠧᆒ"))
            return {}
        if len(bstack1lll11ll1ll_opy_) > 1:
            self.logger.debug(bstack11111_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠࡼ࡮ࡨࡲ࠭ࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᆓ") + str(kwargs) + bstack11111_opy_ (u"ࠨࠢᆔ"))
            return {}
        bstack1lll11ll111_opy_, bstack1lll1ll1111_opy_ = bstack1lll11ll1ll_opy_[0]
        driver = bstack1lll11ll111_opy_()
        if not driver:
            self.logger.debug(bstack11111_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᆕ") + str(kwargs) + bstack11111_opy_ (u"ࠣࠤᆖ"))
            return {}
        capabilities = f.get_state(bstack1lll1ll1111_opy_, bstack1llll1l11l1_opy_.bstack1lll1l1l111_opy_)
        if not capabilities:
            self.logger.debug(bstack11111_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡦࡰࡷࡱࡨࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᆗ") + str(kwargs) + bstack11111_opy_ (u"ࠥࠦᆘ"))
            return {}
        return capabilities.get(bstack11111_opy_ (u"ࠦࡦࡲࡷࡢࡻࡶࡑࡦࡺࡣࡩࠤᆙ"), {})
    def bstack1lll1llll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l11l11_opy_,
        bstack1lllllll1ll_opy_: Tuple[bstack1lll1ll111l_opy_, bstack1lll1l1ll11_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11ll1ll_opy_ = f.get_state(instance, bstack1lll111llll_opy_.bstack1llll111ll1_opy_, [])
        if not bstack1lll1ll1lll_opy_() and len(bstack1lll11ll1ll_opy_) == 0:
            bstack1lll11ll1ll_opy_ = f.get_state(instance, bstack1lll111llll_opy_.bstack1lll1ll11l1_opy_, [])
        if not bstack1lll11ll1ll_opy_:
            self.logger.debug(bstack11111_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣᆚ") + str(kwargs) + bstack11111_opy_ (u"ࠨࠢᆛ"))
            return
        if len(bstack1lll11ll1ll_opy_) > 1:
            self.logger.debug(bstack11111_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾࡰࡪࡴࠨࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡵࠬࢁࠥࡪࡲࡪࡸࡨࡶࡸࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᆜ") + str(kwargs) + bstack11111_opy_ (u"ࠣࠤᆝ"))
        bstack1lll11ll111_opy_, bstack1lll1ll1111_opy_ = bstack1lll11ll1ll_opy_[0]
        driver = bstack1lll11ll111_opy_()
        if not driver:
            self.logger.debug(bstack11111_opy_ (u"ࠤࡪࡩࡹࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡨࡷ࡯ࡶࡦࡴ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᆞ") + str(kwargs) + bstack11111_opy_ (u"ࠥࠦᆟ"))
            return
        return driver